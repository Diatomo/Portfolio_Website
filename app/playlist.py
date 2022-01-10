
import praw
import pprint
import os

def auth():
    reddit = praw.Reddit(
            client_secret=os.environ.get("CLIENT_SECRET"),
            client_id=os.environ.get("CLIENT_ID"),
            user_agent=os.environ.get("USER_AGENT"),
            password=os.environ.get("PASSWORD"),
            username=os.environ.get("USERNAME")
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
    return performances

