import praw
import os

reddit = praw.Reddit(
  clientId     = os.getenv('clientID'),
  clientSecret = os.getenv('clientSecret'),
  username     = os.getenv('username'),
  password     = os.getenv('password'),
  clientId     = os.getenv('clientID'),
  userAgent    = "<EmojiShamerBot1.0>"
)

subreddit = reddit.subreddit("EmojiShamerBot")

for comment in subreddit.stream.comments(skip_existing=True):
    print(comment.body)