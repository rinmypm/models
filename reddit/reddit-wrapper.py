import praw
from configobj import ConfigObj

def main():
    conf = ConfigObj('reddit-config.env')

    reddit = praw.Reddit(client_id=conf['client-id'],
                         client_secret=conf['client-secret'],
                         user_agent=conf['user-agent'])

    # Get top front page listing title
    for submission in reddit.front.hot(limit=20):
        print(submission.title)

if __name__ == "__main__":
    main()
