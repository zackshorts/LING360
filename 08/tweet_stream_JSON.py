import tweepy
import json

# Add your own
consumer_key=""
consumer_secret=""
access_token=""
access_secret=""


# initialize blank list to contain tweets
dodger_tweets = []
# file name that you want to open is the second argument


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        super(tweepy.StreamListener, self).__init__()

        self.save_file = dodger_tweets

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

    def on_data(self, data):
        print(data)
        try:
            with open(output, mode="a") as outfile:
                outfile.write(data)
                return True
        except BaseException as e:
            print("error on data ", e)


output = "dodgers.json"
with open(output, mode="w") as file:
    file.write("")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth, listener=myStreamListener)
myStream.filter(track=['#NationalPancakeDay'])


# auth = tweepy.OAuthHandler("dIiMjbfy1zjUGR6k5IYvRlB5n", "4uJJNKSWCBNsUmj1Xw8GGuz5PCvLdTFG7jdCJWub6IPAtihXXs")
# auth.set_access_token("1074153265086910465-zQEhUqv1AswCmaFnLGrN7cHwgd5HCX",
#                       "k9g8fUiCMzRpdprJjKEMgRJ40DIrJNXDAvDG9N76zpVZo")
#
# api = tweepy.API(auth)
#
# public_tweets = api.home_timeline()
#
# for tweet in public_tweets:
#     print(tweet.text)
