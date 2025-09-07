import praw
username="confused_soul77"
password="apuroop@123"
client_id="OmTYKdbldh_bGDoXlL8asw"
client_secret="NddtVciwLDFzfdcu9gTXhlllo9cVSA"
reddit_instance=praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            username=username,
                            password=password,
                            user_agent="bot_test")
#print(reddit_instance.user.me())
#subreddit = reddit_instance.subreddit("cats")
#top_25_submissions=subreddit.hot(limit=25,time_filter="week")
#for submission in top_25_submissions:
    #print(submission.title)
#subreddit = reddit_instance.subreddit("testingground4bots")
#subreddit.submit(title="test post",selftext="Hello")
submission= reddit_instance.submission("1n9w69z")
comments=submission.comments
print(len(comments))
for comment in comments:
    if "water" in comment.body:
        comment.reply("your comment contains water")