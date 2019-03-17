import json, re, stop_words, statistics
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia


# Holds all of the values of the compound sentiment score of JP Morgan's tweets
all_sentiment = []
# Holds the values of the compound sentiment score or JPM Coin related tweets.
product_sentiment = []
# Holds the negative tweets
negative_tweets = []
# Holds the positive tweets
positive_tweets = []
# Holds the words from the negative tweets
negative_words = {}
# Holds the words from the positive tweets
positive_words = {}


stops = stop_words.get_stop_words('en')
stops.extend(['#jpmorgan', 'jp', '-', '@jpmorgan', '&amp', 'morgan', 'jpmorgan', 'morgan\'s'])


# This function will calculate the sentiment averages for the hashtag and product
# It will also populate the tweet lists.
def calculate_sentiment():
    with open("jpmorgan.json") as json_file:
        for line in json_file:
            tweet = json.loads(line)
            if tweet['lang'] == 'en':
                tweet = tweet['full_text'].lower()
                current_sentiment = sia().polarity_scores(tweet)
                all_sentiment.append(current_sentiment['compound'])
                if current_sentiment['compound'] < 0:
                    negative_tweets.append(tweet)
                elif current_sentiment['compound'] > 0:
                    positive_tweets.append(tweet)
                if re.search('jpmcoin', tweet, flags=re.IGNORECASE):
                    product_sentiment.append(current_sentiment['compound'])
    company_sentiment_mean = statistics.mean(all_sentiment)
    product_sentiment_mean = statistics.mean(product_sentiment)
    print('\nJP Morgan\'s mean sentiment score: ', company_sentiment_mean)
    print('JPM Coin\'s mean sentiment score: ', product_sentiment_mean)
    if product_sentiment_mean > company_sentiment_mean:
        print("As you can see, the product's mean sentiment score is higher than the company's score.\n")
    else:
        print("As you can see, the company's mean sentiment score is higher than the product's score.\n")


# This function will calculate the top words from the positive and negative tweet lists.
def calculate_top_words():
    for tweet in negative_tweets:
        words = tweet.split()
        for word in words:
            word = word.lower()
            if word in stops:
                continue
            elif word in negative_words:
                negative_words[word] += 1
            else:
                negative_words[word] = 1

    for tweet in positive_tweets:
        words = tweet.split()
        for word in words:
            word = word.lower()
            if word in stops:
                continue
            elif word in positive_words:
                positive_words[word] += 1
            else:
                positive_words[word] = 1

    sorted_positive = sorted(positive_words.items(), key=lambda kv: kv[1], reverse=True)
    sorted_negative = sorted(negative_words.items(), key=lambda kv: kv[1], reverse=True)

    print("--- NEGATIVE WORDS ---")
    for i in range(5):
        print(str(i+1) + ". " + str(sorted_negative[i][0]) + " is used " + str(sorted_negative[i][1]) + " times")

    print("\n--- POSITIVE WORDS ---")
    for i in range(5):
        print(str(i+1) + ". " + str(sorted_positive[i][0]) + " is used " + str(sorted_positive[i][1]) + " times")


calculate_sentiment()
calculate_top_words()
