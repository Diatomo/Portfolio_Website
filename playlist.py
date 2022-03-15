
import praw
import pprint
import os
from app import db
from app.models import Tracks 

def auth():
    reddit = praw.Reddit(
        client_secret="qWt2mNuV_9doDaKsBm9FljTqbnZ1Sw",
        client_id="E06qX-Yn4cziFum7J4E8LQ",
        redirect_uri="http://127.0.0.1:5000/playlist",
        user_agent="playlist flask app"
    )
    return reddit

def getPosts(reddit):
    performances = []
    for submission in reddit.subreddit("modular").hot(limit=100):
        performance = {}
        if (submission.is_video and submission.link_flair_text == 'Performance'):
            title = submission.title
            if (len(title) > 35):
                title = title[:35] + '...'
            performance['title'] = title
            performance['score'] = submission.score
            performance['url'] = submission.url
            image = submission.preview['images'][0]['source']['url']
            performance['image'] = image
            audio = submission.media['reddit_video']['fallback_url']
            audio = audio.split('?')[0]
            audio = audio[:audio.find('_')] + '_audio.mp4'
            performance['audio'] = audio
            performance['genre'] = "modular"
            performances.append(performance)
    return performances

def sortDesc(posts):
    return sorted(posts, key=lambda d: d['score'], reverse=True)
    
def prettyPrint(performances):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(performances)

def generate():
    reddit = auth()
    performances = getPosts(reddit)
    performances = sortDesc(performances)
    count = 1
    for performance in performances:
        performance['number'] = count
        count = count + 1
    #prettyPrint(performances)
    insert(performances)
    return performances


def insert(performances):
    addition = False
    for song in performances:
        print("searching through songs")
        exists = db.session.query(Tracks.title).filter_by(title=str(song['title'])).first()
        if (exists is None):
            addition = True
            print("Adding new information")
            print(song['url'])
            track = Tracks(title=song['title'], genre=song['genre'], image=song['image'], audio=song['audio'], url=song['url'], score=song['score'])
            db.session.add(track)

    if (addition == True):
        print("committing new information")
        db.session.commit()


generate()
