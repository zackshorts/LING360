import json, tweepy

consumer_key="dIiMjbfy1zjUGR6k5IYvRlB5n"
consumer_secret="4uJJNKSWCBNsUmj1Xw8GGuz5PCvLdTFG7jdCJWub6IPAtihXXs"
access_token="1074153265086910465-zQEhUqv1AswCmaFnLGrN7cHwgd5HCX"
access_secret="k9g8fUiCMzRpdprJjKEMgRJ40DIrJNXDAvDG9N76zpVZo"

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
