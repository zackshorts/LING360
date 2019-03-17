import re

fin = open('pride.txt', encoding='utf8')
for line in fin:
    if re.search('handsome', line, re.I):
        print(line, '\n')
