import json, csv, re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
count = 0


with open("yelp_AZ_2018.json", encoding="utf8") as json_file, open('Shorts_11.csv', mode='w') as fout:
    fout.write('stars,question_marks,exclamation_points\n')
    for review in json_file:
        count = count + 1
        yelp_review = json.loads(review)

        question_mark_matches = re.findall(r'\?', yelp_review['text'], flags=re.I)
        exclamation_point_matches = re.findall(r'!', yelp_review['text'], flags=re.I)
        num_questions = len(question_mark_matches)
        num_exclamations = len(exclamation_point_matches)

        fout.write(str(yelp_review['stars']) + ',' + str(num_questions) + ',' + str(num_exclamations) + '\n')


yelp = pd.read_csv('Shorts_11.csv', sep=',')
from scipy.stats.stats import pearsonr
correlation_question = pearsonr(yelp.stars, yelp.question_marks)
correlation_exclamation = pearsonr(yelp.stars, yelp.exclamation_points)
seaborn.lmplot(x="question_marks", y="stars", data=yelp, fit_reg=True)
plt.show()
seaborn.lmplot(x="exclamation_points", y="stars", data=yelp, fit_reg=True)
plt.show()
