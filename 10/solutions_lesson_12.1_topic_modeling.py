﻿import os
import re
import gensim
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import pyLDAvis.gensim
import pyLDAvis
from gensim import corpora
import csv
import pandas as pd


# GET ALL FILES IN LIST ###
def file2str(pathway):
    with open(pathway) as infile:
        return infile.read()


os.chdir("./news_universe/")
filenames = [i for i in os.listdir() if re.search(r"\.txt", i)]

doc_complete = [file2str(i) for i in filenames]


# CLEAN UP LIST OF FILES ###
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()


def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


doc_clean = [clean(doc).split() for doc in doc_complete]  


# GET TOPICS ###

# Creating the term dictionary of our corpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
num_topics = 8
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=50)
# print(ldamodel.show_topics(num_topics=num_topics, num_words=10, formatted=True))


# Creat the CSV rows from the ldamodel
def calculateTopTenWords(index):
    word_string = ldamodel.show_topics(num_topics=num_topics, num_words=10, formatted=True)[index][1]
    list_of_words = re.findall('"(\w*)"', word_string)
    return list_of_words


topic_0 = calculateTopTenWords(0)
topic_1 = calculateTopTenWords(1)
topic_2 = calculateTopTenWords(2)
topic_3 = calculateTopTenWords(3)
topic_4 = calculateTopTenWords(4)
topic_5 = calculateTopTenWords(5)
topic_6 = calculateTopTenWords(6)
topic_7 = calculateTopTenWords(7)
os.chdir("../")


def write_to_csv():
    df = pd.DataFrame(list(zip(*[topic_0, topic_1, topic_2, topic_3, topic_4, topic_5, topic_6, topic_7]))).add_prefix('Column ')
    df.to_csv('topics.csv', index=False)
    print(df)


write_to_csv()

# VISUALIZE THE TOPICS ###
### OPTION 1: ForceAtlas2 algorithm (code from Rob Reynolds: https://github.com/reynoldsnlp/F18_DIGHT360/blob/master/activities/12_04_topic_modeling.py)

# from fa2 import ForceAtlas2  # pip install fa2
# import matplotlib.pyplot as plt
# import networkx as nx
#
# rows = []
# for i in range(0, len(doc_term_matrix)):
#     doc_topics = ldamodel.get_document_topics(doc_term_matrix[i])
#     for topic in doc_topics:
#         row = [filenames[i], topic[0], topic[1]]
#         rows.append(row)
#
# edges = [(i[0][8:-5], i[1], i[2]) for i in rows]
#
# g = nx.Graph()
# g.add_weighted_edges_from(edges)
# # print(g.edges())
#
# forceatlas2 = ForceAtlas2(# Behavior alternatives  # noqa: E261
#                           outboundAttractionDistribution=False,  # Dissuade hubs
#                           linLogMode=False,  # NOT IMPLEMENTED
#                           adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
#                           edgeWeightInfluence=1.0,
#
#                           # Performance
#                           jitterTolerance=1.0,  # Tolerance
#                           barnesHutOptimize=True,
#                           barnesHutTheta=1.2,
#                           multiThreaded=False,  # NOT IMPLEMENTED
#
#                           # Tuning
#                           scalingRatio=2.0,
#                           strongGravityMode=False,
#                           gravity=4.0,
#
#                           # Log
#                           verbose=True)
#
# positions = forceatlas2.forceatlas2_networkx_layout(g, pos=None, iterations=2000)
# print(positions)
# nx.draw_networkx(g, positions, cmap=plt.get_cmap('jet'), node_size=75, with_labels=True, font_size=8, label=f'Topics')
# plt.show()


# OPTION 2: interactive display with D3 javascript library
to_show = pyLDAvis.gensim.prepare(ldamodel, doc_term_matrix, dictionary)
pyLDAvis.show(to_show)

