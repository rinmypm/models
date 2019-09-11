import praw
from configobj import ConfigObj

conf = ConfigObj('reddit-config.env')

reddit = praw.Reddit(client_id=conf['client-id'],
                     client_secret=conf['client-secret'],
                     user_agent=conf['user-agent'])

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)

