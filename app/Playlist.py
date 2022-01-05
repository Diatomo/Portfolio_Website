
import praw
import pprint


class Playlist:

    def __init__(self):
        pass

    def auth(self):
        reddit = praw.Reddit(
                client_secret="AmrUgTbx_RvUNX7aSh_ab4OQL_KGeg",
                client_id="OBHuCQdkUg2oPpGlf61dcA",
                user_agent="modular_script",
                password="Nomino253!",
                username="Diatomo"
        )
        return reddit

    def getPosts(self, reddit):
        performances = []
        for submission in reddit.subreddit("modular").hot(limit=200):
            performance = {'score' : None, 'url' : None}
            if (submission.is_video and submission.link_flair_text == 'Performance'):
                performance['title'] = submission.title
                performance['score'] = submission.score
                performance['url'] = submission.url
                performances.append(performance)
        return performances

    def sortDesc(self, posts):
        return sorted(posts, key=lambda d: d['score'], reverse=True)
        
    def prettyPrint(self, performances):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(performances)

    def generate(self):
        reddit = self.auth()
        performances = self.getPosts(reddit)
        performances = self.sortDesc(performances)
        self.prettyPrint(performances)

