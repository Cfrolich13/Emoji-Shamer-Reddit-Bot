import praw
import os

reddit = praw.Reddit(
  client_id     = os.getenv('client_id'),
  client_secret = os.getenv('client_secret'),
  username      = os.getenv('username'),
  password      = os.getenv('password'),
  user_agent    = "<EmojiShamerBot1.0>"
)

class redditBot:
    def findMatch(self, comment):
        if '🤓' in comment.body:
            print(comment.body)
            self.makeReply(comment)
    
    def commentUpvoteCheck(self):
        pass
    
    def makeReply(self, comment):
        try:
            comment.reply("You used the forbidden emoji. As I'm still in beta, I spared the downvote. You can thank me later.")
        except Exception as e:
            print(e)

bot = redditBot()

subreddit = reddit.subreddit("EmojiShamerBot")

for comment in subreddit.stream.comments(skip_existing=True):
    #print(comment.body)
    bot.findMatch(comment)