import json, csv, re
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

wednesdays = 0
saturdays = 0
count = 0
wednesday_stars = 0
saturday_stars = 0

with open("yelp_AZ_2018.json", encoding="utf8") as json_file, open('yelp.csv', mode='w') as fout:
    dates = []

    fout.write('stars,delicious\n')
    for review in json_file:
        count = count + 1
        yelp_review = json.loads(review)

        matches = re.findall(r'\bdelicious\b', yelp_review['text'], flags=re.I)
        matches_2 = re.findall(r'([aeiou])\1{2,}', yelp_review['text'], flags=re.I)
        num_matches = len(matches)
        fout.write(str(yelp_review['stars']) + ',' + str(num_matches) + '\n')

        if dt.strptime(yelp_review['date'], '%Y-%m-%d %H:%M:%S').weekday() == 2:
            wednesdays += 1
            wednesday_stars += yelp_review['stars']
        elif dt.strptime(yelp_review['date'], '%Y-%m-%d %H:%M:%S').weekday() == 5:
            saturdays += 1
            saturday_stars += yelp_review['stars']
        dates.append(yelp_review['date'])


print("\nWednesday Star Average: " + str(wednesday_stars/wednesdays))
print("Saturday Star Average: " + str(saturday_stars/saturdays) + '\n\n')

print("Wednesdays: " + str(wednesdays))
print("Saturdays: " + str(saturdays) + '\n\n')

dates.sort()
first_date = dates[0]
last_date = dates[-1]

print("First: " + first_date)
print("Last: " + last_date)


yelp = pd.read_csv('yelp.csv', sep=',')
from scipy.stats.stats import pearsonr
correlation = pearsonr(yelp.stars, yelp.delicious)
print(correlation)

seaborn.lmplot(x="delicious", y="stars", data = yelp, fit_reg=True)
plt.show()
