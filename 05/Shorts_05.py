import os
import csv
import re
import stop_words
from collections import Counter

# Change directory to where the corpus array are held
directory = './Mini-CORE_new'
os.chdir(directory)

# Initialize the corpus component arrays
HI_array = []
ID_array = []
IN_array = []
IP_array = []
LY_array = []
NA_array = []
OP_array = []
SP_array = []

count = 0


def write_to_csv(dictionary, csv_file_name):
    sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
    with open(csv_file_name + '.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(sorted_dictionary)


# function to read in the file contents
def read_in_file(fn):
    with open(fn, 'rb') as f:
        # Start after the header is read in
        for index in range(6):
            next(f)
        t = f.read()
        t = str(t)[1:]
    return t


# Construct each individual array for each component of corpus.
for filename in os.listdir():
    try:
        if filename.endswith(".txt") and filename.startswith('1+HI'):
            text = read_in_file(filename)
            HI_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+ID'):
            text = read_in_file(filename)
            ID_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+IN'):
            text = read_in_file(filename)
            IN_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+IP'):
            text = read_in_file(filename)
            IP_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+LY'):
            text = read_in_file(filename)
            LY_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+NA'):
            text = read_in_file(filename)
            NA_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+OP'):
            text = read_in_file(filename)
            OP_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+SP'):
            text = read_in_file(filename)
            SP_array.append(text)
    except Exception as e:
        count += 1

HI_words = {}
ID_words = {}
IN_words = {}
IP_words = {}
LY_words = {}
NA_words = {}
OP_words = {}
SP_words = {}

stops = stop_words.get_stop_words('en')

for string in HI_array:
    split_string = string.split()
    for word in split_string:
        word = word.lower()
        if word in stops:
            continue
        elif word in HI_words:
            HI_words[word] += 1
        else:
            HI_words[word] = 1

for string in ID_array:
    split_string = string.split()
    for word in split_string:
        word = word.lower()
        if word in stops:
            continue
        elif word in ID_words:
            ID_words[word] += 1
        else:
            ID_words[word] = 1

for string in IN_array:
    string = re.sub('[^a-zA-Z\s]', '', string)
    string = re.sub('rnp', '', string)
    split_string = string.split()

    for word in split_string:
        word = word.lower()
        if word in stops:
            continue
        elif word in IN_words:
            IN_words[word] += 1
        else:
            IN_words[word] = 1

for string in IP_array:
    split_string = string.split()
    for word in split_string:
        word = word.lower()
        if word in stops:
            continue
        elif word in IP_words:
            IP_words[word] += 1
        else:
            IP_words[word] = 1

for string in LY_array:
    split_string = string.split()
    for word in split_string:
        word = word.lower()
        if word in stops:
            continue
        elif word in LY_words:
            LY_words[word] += 1
        else:
            LY_words[word] = 1

for string in NA_array:
    split_string = string.split()
    for word in split_string:
        word = word.lower()
        if word in stops:
            continue
        elif word in NA_words:
            NA_words[word] += 1
        else:
            NA_words[word] = 1

for string in OP_array:
    split_string = string.split()
    for word in split_string:
        word = word.lower()
        if word in stops:
            continue
        elif word in OP_words:
            OP_words[word] += 1
        else:
            OP_words[word] = 1

for string in SP_array:
    split_string = string.split()
    for word in split_string:
        word = word.lower()
        if word in stops:
            continue
        elif word in SP_words:
            SP_words[word] += 1
        else:
            SP_words[word] = 1

os.chdir('../output')
write_to_csv(HI_words, 'HI_word_count')
print("HI word count generated")
write_to_csv(ID_words, 'ID_word_count')
print("ID word count generated")
write_to_csv(IN_words, 'IN_word_count')
print("IN word count generated")
write_to_csv(IP_words, 'IP_word_count')
print("IP word count generated")
write_to_csv(LY_words, 'LY_word_count')
print("LY word count generated")
write_to_csv(NA_words, 'NA_word_count')
print("NA word count generated")
write_to_csv(OP_words, 'OP_word_count')
print("OP word count generated")
write_to_csv(SP_words, 'SP_word_count')
print("SP word count generated")
