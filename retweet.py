import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def main():
    search = ("#mathematician")
 
    numberofTweets = 10
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        if not tweet.retweeted or not tweet.favorited:
            
            try:
                tweet.favorite()
                tweet.retweet()
                print("Tweet Retweeted")
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
main()

"""
import schedule  

def job():  
    print("A Simple Python Scheduler.")  

# run the function job() every 30 minutes  
schedule.every(30).minutes.do(job)  

while True:  
    schedule.run_pending()  """