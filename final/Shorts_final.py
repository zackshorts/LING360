import os, string, statistics, pandas as pd
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
# Reset this variable every time a letter is done
paragraph_count = 1

# Loop through the paragraphs in 2017
for paragraph in letter2017.split("\n"):
    if paragraph == '':
        continue
    all_sentiment = []
    # Loop through the words in the paragraph
    for word in paragraph.split():
        current_sentiment = sia().polarity_scores(word)
        all_sentiment.append(current_sentiment['compound'])
    #     Add that paragraphs data to the 2017 data file
    data_2017.append([statistics.mean(all_sentiment), paragraph_count])
    # This keeps track of where you are in the letter
    paragraph_count += 1
    print(paragraph)
#     Creates a dataframe so we can plot the data later on
df_2017 = pd.DataFrame(data_2017, columns=['Sentiment', 'Paragraph'])
paragraph_count = 1

# Loop through the paragraphs in 2018
for paragraph in letter2018.split("\n"):
    if paragraph == '':
        continue
    all_sentiment = []
    # Loop through the words in the paragraph
    for word in paragraph.split():
        current_sentiment = sia().polarity_scores(word)
        all_sentiment.append(current_sentiment['compound'])
    # Add that paragraphs data to the 2018 data file
    data_2018.append([statistics.mean(all_sentiment), paragraph_count])
    paragraph_count += 1
    # This keeps track of where you are in the letter
    print(paragraph)
#     Creates a dataframe so we can plot the data later on
df_2018 = pd.DataFrame(data_2018, columns=['Sentiment', 'Paragraph'])

# Plots the data as a lineplot
plot2017 = seaborn.lineplot(x="Paragraph", y="Sentiment", data=df_2017)
plot2017.set_title("2017 JPMorgan Annual Report")
plt.show()
plot2018 = seaborn.lineplot(x="Paragraph", y="Sentiment", data=df_2018)
plot2018.set_title("2018 JPMorgan Annual Report")
plt.show()
