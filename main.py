import praw
import os

reddit = praw.Reddit(
  client_id     = os.getenv('client_id'),
  client_secret = os.getenv('client_secret'),
  username      = os.getenv('username'),
  password      = os.getenv('password'),
  user_agent    = "<EmojiShamerBot1.0>"
)

subreddit = reddit.subreddit("EmojiShamerBot")

for comment in subreddit.stream.comments(skip_existing=True):
    print(comment.body)