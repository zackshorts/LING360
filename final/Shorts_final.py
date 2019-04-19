import os, re, string, json, statistics, pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn


def file2str(pathway):
    with open(pathway) as infile:
        return infile.read()


# CLEAN UP LIST OF FILES ###
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


# Change directory to output and save the contents of txt file as a string.
# Initializes the variables that we will need
os.chdir("./output/")
letter2017 = file2str("2017.txt")
letter2018 = file2str("2018.txt")
# These bits of data will be in this format ---- ['sentiment score of paragraph', paragraph number]
data_2018 = []
data_2017 = []
current_sentiment = []
all_sentiment = []
paragraph_count = 1

for paragraph in letter2017.split("\n"):
    if paragraph == '':
        continue
    length = len(paragraph.split())
    all_sentiment = []
    for word in paragraph.split():
        current_sentiment = sia().polarity_scores(word)
        all_sentiment.append(current_sentiment['compound'])
    data_2017.append([statistics.mean(all_sentiment), paragraph_count])
    paragraph_count += 1
    print(length)
    print(paragraph)
df_2017 = pd.DataFrame(data_2017, columns=['Sentiment', 'Paragraph'])
paragraph_count = 1
for paragraph in letter2018.split("\n"):
    if paragraph == '':
        continue
    length = len(paragraph.split())
    all_sentiment = []
    for word in paragraph.split():
        current_sentiment = sia().polarity_scores(word)
        all_sentiment.append(current_sentiment['compound'])
    data_2018.append([statistics.mean(all_sentiment), paragraph_count])
    paragraph_count += 1
    print(length)
    print(paragraph)
df_2018 = pd.DataFrame(data_2018, columns=['Sentiment', 'Paragraph'])


plot2017 = seaborn.lineplot(x="Paragraph", y="Sentiment", data=df_2017)
plot2017.set_title("2017 JPMorgan Annual Report")
plt.show()
plot2018 = seaborn.lineplot(x="Paragraph", y="Sentiment", data=df_2018)
plot2018.set_title("2018 JPMorgan Annual Report")
plt.show()
