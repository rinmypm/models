import praw
from configobj import ConfigObj
from urllib.parse import quote_plus

QUESTIONS = ["what is", "who is", "what are"]
REPLY_TEMPLATE = "[Let me google that for you](http://lmgtfy.com/?q={})"

def main():
    conf = ConfigObj('reddit-config.env')

    reddit = praw.Reddit(client_id=conf['client-id'],
                         client_secret=conf['client-secret'],
                         user_agent=conf['user-agent'],
                         username=conf['username'],
                         password=conf['password'])

    subreddit = reddit.subreddit("AskReddit")
    for submission in subreddit.stream.submissions():
        process_submission(submission)

def process_submission(submission):
    # Ignore titles with more than 10 words as they probably are not simple
    # questions.
    if len(submission.title.split()) > 10:
        return

    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print("Replying to: {}".format(submission.title))
            submission.reply(reply_text)
            # A reply has been made so do not attempt to match other phrases.
            break

if __name__ == "__main__":
    main()