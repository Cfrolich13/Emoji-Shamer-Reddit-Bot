import praw
import os

reddit = praw.Reddit(
  clientId = os.getenv('clientID')
)