import nltk, csv, re, os

# Change to corpus
os.chdir('./AWE_untagd')

# Initialize lists that are filled with every word
JA_BI_array = []
JA_HI_array = []
PS_BI_array = []
PS_HI_array = []
TB_BI_array = []
TB_HI_array = []

count = 0


# function to read in the file contents
def read_in_file(fn):
    with open(fn, 'rb') as f:
        # Start after the header is read in
        for index in range(10):
            next(f)
        t = f.read()
        t = str(t)[1:]
    return t


# This function will take a list and convert it to a csv file
def write_to_csv(csv_array, csv_file_name):
    with open(csv_file_name + '.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csv_array)


for filename in os.listdir():
    try:
        if filename.endswith(".txt") and filename.startswith('JA_BI'):
            text = read_in_file(filename)
            JA_BI_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('JA_HI'):
            text = read_in_file(filename)
            JA_HI_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('PS_BI'):
            text = read_in_file(filename)
            PS_BI_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('PS_HI'):
            text = read_in_file(filename)
            PS_HI_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('TB_BI'):
            text = read_in_file(filename)
            TB_BI_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('TB_HI'):
            text = read_in_file(filename)
            TB_HI_array.append(text)
    except Exception as e:
        count += 1


JA_BI_words = {}
JA_HI_words = {}
PS_BI_words = {}
PS_HI_words = {}
TB_BI_words = {}
TB_HI_words = {}

TOTAL_JA_BI_words = 0
TOTAL_JA_HI_words = 0
TOTAL_PS_BI_words = 0
TOTAL_PS_HI_words = 0
TOTAL_TB_BI_words = 0
TOTAL_TB_HI_words = 0

CSV_JA_BI_words = []
CSV_JA_HI_words = []
CSV_PS_BI_words = []
CSV_PS_HI_words = []
CSV_TB_BI_words = []
CSV_TB_HI_words = []


# This function will create the dictionary for each type of file and the total words in each one
def calculate_dictionary(array, dictionary, total):
    for string in array:
        total += len(string)
        string = re.sub('[\n]+|[\r]+|[.,/)(%^&*$#@!+="]', ' ', string)
        split_string = string.split()
        looking_for_first = True
        looking_for_second = False
        key = ""
        for word, pos in nltk.pos_tag(split_string):
            word = word.lower()
            if pos == "NN" and looking_for_first:
                key = word + " "
                looking_for_first = False
                looking_for_second = True
                continue
            if pos == "NN" and looking_for_second:
                key += word
                looking_for_second = False
                looking_for_first = True
                if key in dictionary:
                    dictionary[key] += 1
                else:
                    dictionary[key] = 1
    dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
    return dictionary, total


# This function will convert the dictionary and count into a list that will eventually be converted to CSV format
def make_csv_array(dictionary, new_array, count):
    for record in dictionary:
        freq = record[1]
        record = record[0].split(' ')
        new_array.append([record[0], record[1], 1000*freq/count])
    return new_array


# These lines will calculate the dictionary, list and count for each type of file
JA_BI_words, TOTAL_JA_BI_words = calculate_dictionary(JA_BI_array, JA_BI_words, TOTAL_JA_BI_words)
CSV_JA_BI_words = make_csv_array(JA_BI_words, CSV_JA_BI_words, TOTAL_JA_BI_words)

JA_HI_words, TOTAL_JA_HI_words = calculate_dictionary(JA_HI_array, JA_HI_words, TOTAL_JA_HI_words)
CSV_JA_HI_words = make_csv_array(JA_HI_words, CSV_JA_HI_words, TOTAL_JA_HI_words)

PS_BI_words, TOTAL_PS_BI_words = calculate_dictionary(PS_BI_array, PS_BI_words, TOTAL_PS_BI_words)
CSV_PS_BI_words = make_csv_array(PS_BI_words, CSV_PS_BI_words, TOTAL_PS_BI_words)

PS_HI_words, TOTAL_PS_HI_words = calculate_dictionary(PS_HI_array, PS_HI_words, TOTAL_PS_HI_words)
CSV_PS_HI_words = make_csv_array(PS_HI_words, CSV_PS_HI_words, TOTAL_PS_HI_words)

TB_BI_words, TOTAL_TB_BI_words = calculate_dictionary(TB_BI_array, TB_BI_words, TOTAL_TB_BI_words)
CSV_TB_BI_words = make_csv_array(TB_BI_words, CSV_TB_BI_words, TOTAL_TB_BI_words)

TB_HI_words, TOTAL_TB_HI_words = calculate_dictionary(TB_HI_array, TB_HI_words, TOTAL_TB_HI_words)
CSV_TB_HI_words = make_csv_array(TB_HI_words, CSV_TB_HI_words, TOTAL_TB_HI_words)

# These lines will convert the lists to cvs files
os.chdir('../output')
write_to_csv(CSV_JA_BI_words, 'JA_BI')
write_to_csv(CSV_JA_HI_words, 'JA_HI')
write_to_csv(CSV_PS_BI_words, 'PS_BI')
write_to_csv(CSV_PS_HI_words, 'PS_HI')
write_to_csv(CSV_TB_BI_words, 'TB_BI')
write_to_csv(CSV_TB_HI_words, 'TB_HI')
