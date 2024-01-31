# mozna wybrac post na redicie, potem w settingsach konta trzeba sworzyć sobie personal key zeby moc scrapować
# dane z tego postu
from datetime import datetime, timedelta

import praw

reddit = praw.Reddit(user_agent=True,
                     client_id="xxx",
                     client_secret="YYY",
                     username='nazwa_usera',
                     password='password')

url = "https://www.reddit.com/r/BaldursGate3/comments/19exv4w/nettie_cant_be_a_very_good_healer/"

post = reddit.submission(url=url)
print(post.title)
print(post.selftext)

for comment in post.comments:
    print(comment.body)

### Get all posts of the last 24h

subreddit = reddit.subreddit("glassblowing")

post24h = []
for post in subreddit.new():
    current_time = datetime.utcnow()
    post_time = datetime.utcfromtimestamp(post.created)
    # print(current_time, post_time)

    delta_time = current_time - post_time
    if delta_time <= timedelta(hours=24):
        post24h.append((post.title, post.selftext, post.created))

### Create a new post

