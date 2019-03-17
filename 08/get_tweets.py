import json, tweepy

# Add your own
consumer_key=""
consumer_secret=""
access_token=""
access_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

hashtag = "jpmorgan"

tweets = tweepy.Cursor(api.search, q="#"+hashtag+"-filter:retweets", tweet_mode='extended').items(1000)

output = hashtag + ".json"
with open(output, mode="w", encoding="utf8") as file:
    for tweet in tweets:
        file.write(json.dumps(tweet._json))
        file.write("\n")
