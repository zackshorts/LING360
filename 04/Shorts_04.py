import os
import csv
import re

# Change directory to where the corpus array are held
directory = './Mini-CORE_new'
os.chdir(directory)

# INitialize the corpus component arrays
HI_array = []
ID_array = []
IN_array = []
IP_array = []
LY_array = []
NA_array = []
OP_array = []
SP_array = []

count = 0

# Construct each individual array for each component of corpus.
for filename in os.listdir():
    try:
        if filename.endswith(".txt") and filename.startswith('1+HI'):
            with open(filename, 'rb') as f:
                # Start after the header is read in
                for i in range(6):
                    next(f)
                text = f.read()
                text = str(text)[1:]
            HI_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+ID'):
            with open(filename, 'rb+') as f:
                for i in range(6):
                    next(f)
                text = f.read()
                text = str(text)[1:]
            ID_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+IN'):
            with open(filename, 'rb+') as f:
                for i in range(6):
                    next(f)
                text = f.read()
                text = str(text)[1:]
            IN_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+IP'):
            with open(filename, 'rb+') as f:
                for i in range(6):
                    next(f)
                text = f.read()
                text = str(text)[1:]
            IP_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+LY'):
            with open(filename, 'rb+') as f:
                for i in range(6):
                    next(f)
                text = f.read()
                text = str(text)[1:]
            LY_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+NA'):
            with open(filename, 'rb+') as f:
                for i in range(6):
                    next(f)
                text = f.read()
                text = str(text)[1:]
            NA_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+OP'):
            with open(filename, 'rb+') as f:
                for i in range(6):
                    next(f)
                text = f.read()
                text = str(text)[1:]
            OP_array.append(text)
        elif filename.endswith(".txt") and filename.startswith('1+SP'):
            with open(filename, 'rb+') as f:
                for i in range(6):
                    next(f)
                text = f.read()
                text = str(text)[1:]
            SP_array.append(text)
    except Exception as e:
        count += 1

# Contraction Count
HI_word_count = 0
HI_contraction_count = 0
for string in HI_array:
    HI_word_count += len(string.split())
    HI_contraction_count += len(re.findall(
        "/they've|aren't|can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|he'd|he'll|he's|i'd|i'll|i'm|i've|isn't|let's|mightn't|mustn't|shan't|she'd|she'll|she's|shouldn't|that's|there's|they'd|they'll|they're|we'd|we're|we've|weren't|what'll|what're|what's|what've|where's|who's|who'll|who're|who's|who've|won't|wouldn't|you'd|you'll|you're|you've|it's|everything's|there'll|we'll", string))
HI_normalized_contraction_count = HI_contraction_count/(HI_word_count/1000)
print("Number of contractions per 1000 words in HI: " + str(HI_normalized_contraction_count))

ID_word_count = 0
ID_contraction_count = 0
for string in ID_array:
    ID_word_count += len(string.split())
    ID_contraction_count += len(re.findall("/they've|aren't|can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|he'd|he'll|he's|i'd|i'll|i'm|i've|isn't|let's|mightn't|mustn't|shan't|she'd|she'll|she's|shouldn't|that's|there's|they'd|they'll|they're|we'd|we're|we've|weren't|what'll|what're|what's|what've|where's|who's|who'll|who're|who's|who've|won't|wouldn't|you'd|you'll|you're|you've|it's|everything's|there'll|we'll", string))
ID_normalized_contraction_count = ID_contraction_count/(ID_word_count/1000)
print("Number of contractions per 1000 words in ID: " + str(ID_normalized_contraction_count))

IN_word_count = 0
IN_contraction_count = 0
for string in IN_array:
    IN_word_count += len(string.split())
    IN_contraction_count += len(re.findall("/they've|aren't|can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|he'd|he'll|he's|i'd|i'll|i'm|i've|isn't|let's|mightn't|mustn't|shan't|she'd|she'll|she's|shouldn't|that's|there's|they'd|they'll|they're|we'd|we're|we've|weren't|what'll|what're|what's|what've|where's|who's|who'll|who're|who's|who've|won't|wouldn't|you'd|you'll|you're|you've|it's|everything's|there'll|we'll", string))
IN_normalized_contraction_count = IN_contraction_count/(IN_word_count/1000)
print("Number of contractions per 1000 words in IN: " + str(IN_normalized_contraction_count))

IP_word_count = 0
IP_contraction_count = 0
for string in IP_array:
    IP_word_count += len(string.split())
    IP_contraction_count += len(re.findall("/they've|aren't|can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|he'd|he'll|he's|i'd|i'll|i'm|i've|isn't|let's|mightn't|mustn't|shan't|she'd|she'll|she's|shouldn't|that's|there's|they'd|they'll|they're|we'd|we're|we've|weren't|what'll|what're|what's|what've|where's|who's|who'll|who're|who's|who've|won't|wouldn't|you'd|you'll|you're|you've|it's|everything's|there'll|we'll", string))
IP_normalized_contraction_count = IP_contraction_count/(IP_word_count/1000)
print("Number of contractions per 1000 words in IP: " + str(IP_normalized_contraction_count))

LY_word_count = 0
LY_contraction_count = 0
for string in LY_array:
    LY_word_count += len(string.split())
    LY_contraction_count += len(re.findall("/they've|aren't|can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|he'd|he'll|he's|i'd|i'll|i'm|i've|isn't|let's|mightn't|mustn't|shan't|she'd|she'll|she's|shouldn't|that's|there's|they'd|they'll|they're|we'd|we're|we've|weren't|what'll|what're|what's|what've|where's|who's|who'll|who're|who's|who've|won't|wouldn't|you'd|you'll|you're|you've|it's|everything's|there'll|we'll", string))
LY_normalized_contraction_count = LY_contraction_count/(LY_word_count/1000)
print("Number of contractions per 1000 words in LY: " + str(LY_normalized_contraction_count))

NA_word_count = 0
NA_contraction_count = 0
for string in NA_array:
    NA_word_count += len(string.split())
    NA_contraction_count += len(re.findall("/they've|aren't|can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|he'd|he'll|he's|i'd|i'll|i'm|i've|isn't|let's|mightn't|mustn't|shan't|she'd|she'll|she's|shouldn't|that's|there's|they'd|they'll|they're|we'd|we're|we've|weren't|what'll|what're|what's|what've|where's|who's|who'll|who're|who's|who've|won't|wouldn't|you'd|you'll|you're|you've|it's|everything's|there'll|we'll", string))
NA_normalized_contraction_count = NA_contraction_count/(NA_word_count/1000)
print("Number of contractions per 1000 words in NA: " + str(NA_normalized_contraction_count))

OP_word_count = 0
OP_contraction_count = 0
for string in OP_array:
    OP_word_count += len(string.split())
    OP_contraction_count += len(re.findall("/they've|aren't|can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|he'd|he'll|he's|i'd|i'll|i'm|i've|isn't|let's|mightn't|mustn't|shan't|she'd|she'll|she's|shouldn't|that's|there's|they'd|they'll|they're|we'd|we're|we've|weren't|what'll|what're|what's|what've|where's|who's|who'll|who're|who's|who've|won't|wouldn't|you'd|you'll|you're|you've|it's|everything's|there'll|we'll", string))
OP_normalized_contraction_count = OP_contraction_count/(OP_word_count/1000)
print("Number of contractions per 1000 words in OP: " + str(OP_normalized_contraction_count))

SP_word_count = 0
SP_contraction_count = 0
for string in SP_array:
    SP_word_count += len(string.split())
    SP_contraction_count += len(re.findall("/they've|aren't|can't|couldn't|didn't|doesn't|don't|hadn't|hasn't|haven't|he'd|he'll|he's|i'd|i'll|i'm|i've|isn't|let's|mightn't|mustn't|shan't|she'd|she'll|she's|shouldn't|that's|there's|they'd|they'll|they're|we'd|we're|we've|weren't|what'll|what're|what's|what've|where's|who's|who'll|who're|who's|who've|won't|wouldn't|you'd|you'll|you're|you've|it's|everything's|there'll|we'll", string))
SP_normalized_contraction_count = SP_contraction_count/(SP_word_count/1000)
print("Number of contractions per 1000 words in SP: " + str(SP_normalized_contraction_count))

# Modal Count
HI_word_count = 0
HI_modal_count = 0
for string in HI_array:
    HI_word_count += len(string.split())
    HI_modal_count += len(re.findall('/can|could|may|might|will|would|shall|should|must/', string))
HI_normalized_modal_count = HI_modal_count/(HI_word_count/1000)
print("Number of modals per 1000 words in HI: " + str(HI_normalized_modal_count))

ID_word_count = 0
ID_modal_count = 0
for string in ID_array:
    ID_word_count += len(string.split())
    ID_modal_count += len(re.findall('/can|could|may|might|will|would|shall|should|must/', string))
ID_normalized_modal_count = ID_modal_count/(ID_word_count/1000)
print("Number of modals per 1000 words in ID: " + str(ID_normalized_modal_count))

IN_word_count = 0
IN_modal_count = 0
for string in IN_array:
    IN_word_count += len(string.split())
    IN_modal_count += len(re.findall('/can|could|may|might|will|would|shall|should|must/', string))
IN_normalized_modal_count = IN_modal_count/(IN_word_count/1000)
print("Number of modals per 1000 words in IN: " + str(IN_normalized_modal_count))

IP_word_count = 0
IP_modal_count = 0
for string in IP_array:
    IP_word_count += len(string.split())
    IP_modal_count += len(re.findall('/can|could|may|might|will|would|shall|should|must/', string))
IP_normalized_modal_count = IP_modal_count/(IP_word_count/1000)
print("Number of modals per 1000 words in IP: " + str(IP_normalized_modal_count))

LY_word_count = 0
LY_modal_count = 0
for string in LY_array:
    LY_word_count += len(string.split())
    LY_modal_count += len(re.findall('/can|could|may|might|will|would|shall|should|must/', string))
LY_normalized_modal_count = LY_modal_count/(LY_word_count/1000)
print("Number of modals per 1000 words in LY: " + str(LY_normalized_modal_count))

NA_word_count = 0
NA_modal_count = 0
for string in NA_array:
    NA_word_count += len(string.split())
    NA_modal_count += len(re.findall('/can|could|may|might|will|would|shall|should|must/', string))
NA_normalized_modal_count = NA_modal_count/(NA_word_count/1000)
print("Number of modals per 1000 words in NA: " + str(NA_normalized_modal_count))

OP_word_count = 0
OP_modal_count = 0
for string in OP_array:
    OP_word_count += len(string.split())
    OP_modal_count += len(re.findall('/can|could|may|might|will|would|shall|should|must/', string))
OP_normalized_modal_count = OP_modal_count/(OP_word_count/1000)
print("Number of modals per 1000 words in OP: " + str(OP_normalized_modal_count))

SP_word_count = 0
SP_modal_count = 0
for string in SP_array:
    SP_word_count += len(string.split())
    SP_modal_count += len(re.findall('/can|could|may|might|will|would|shall|should|must/', string))
SP_normalized_modal_count = SP_modal_count/(SP_word_count/1000)
print("Number of modals per 1000 words in SP: " + str(SP_normalized_modal_count))

# Pronoun Count
HI_word_count = 0
HI_pronoun_count = 0
for string in HI_array:
    HI_word_count += len(string.split())
    HI_pronoun_count += len(re.findall('/i|he|she|we|you|they/', string))
HI_normalized_pronoun_count = HI_pronoun_count/(HI_word_count/1000)
print("Number of pronouns per 1000 words in HI: " + str(HI_normalized_pronoun_count))

ID_word_count = 0
ID_pronoun_count = 0
for string in ID_array:
    ID_word_count += len(string.split())
    ID_pronoun_count += len(re.findall('/i|he|she|we|you|they/', string))
ID_normalized_pronoun_count = ID_pronoun_count/(ID_word_count/1000)
print("Number of pronouns per 1000 words in ID: " + str(ID_normalized_pronoun_count))

IN_word_count = 0
IN_pronoun_count = 0
for string in IN_array:
    IN_word_count += len(string.split())
    IN_pronoun_count += len(re.findall('/i|he|she|we|you|they/', string))
IN_normalized_pronoun_count = IN_pronoun_count/(IN_word_count/1000)
print("Number of pronouns per 1000 words in IN: " + str(IN_normalized_pronoun_count))

IP_word_count = 0
IP_pronoun_count = 0
for string in IP_array:
    IP_word_count += len(string.split())
    IP_pronoun_count += len(re.findall('/i|he|she|we|you|they/', string))
IP_normalized_pronoun_count = IP_pronoun_count/(IP_word_count/1000)
print("Number of pronouns per 1000 words in IP: " + str(IP_normalized_pronoun_count))

LY_word_count = 0
LY_pronoun_count = 0
for string in LY_array:
    LY_word_count += len(string.split())
    LY_pronoun_count += len(re.findall('/i|he|she|we|you|they/', string))
LY_normalized_pronoun_count = LY_pronoun_count/(LY_word_count/1000)
print("Number of pronouns per 1000 words in LY: " + str(LY_normalized_pronoun_count))

NA_word_count = 0
NA_pronoun_count = 0
for string in NA_array:
    NA_word_count += len(string.split())
    NA_pronoun_count += len(re.findall('/i|he|she|we|you|they/', string))
NA_normalized_pronoun_count = NA_pronoun_count/(NA_word_count/1000)
print("Number of pronouns per 1000 words in NA: " + str(NA_normalized_pronoun_count))

OP_word_count = 0
OP_pronoun_count = 0
for string in OP_array:
    OP_word_count += len(string.split())
    OP_pronoun_count += len(re.findall('/i|he|she|we|you|they/', string))
OP_normalized_pronoun_count = OP_pronoun_count/(OP_word_count/1000)
print("Number of pronouns per 1000 words in OP: " + str(OP_normalized_pronoun_count))

SP_word_count = 0
SP_pronoun_count = 0
for string in SP_array:
    SP_word_count += len(string.split())
    SP_pronoun_count += len(re.findall('/i|he|she|we|you|they/', string))
SP_normalized_pronoun_count = SP_pronoun_count/(SP_word_count/1000)
print("Number of pronouns per 1000 words in SP: " + str(SP_normalized_pronoun_count))


# Write to CSV
csvData = [['Register', 'Contractions', 'Modals', 'Pronouns'], ['HI', HI_normalized_contraction_count, HI_normalized_modal_count, HI_normalized_pronoun_count], ['ID', ID_normalized_contraction_count, ID_normalized_modal_count, ID_normalized_pronoun_count], ['IN', IN_normalized_contraction_count, IN_normalized_modal_count, IN_normalized_pronoun_count], ['IP', IP_normalized_contraction_count, IP_normalized_modal_count, IP_normalized_pronoun_count], ['LY', LY_normalized_contraction_count, LY_normalized_modal_count, LY_normalized_pronoun_count], ['NA', NA_normalized_contraction_count, NA_normalized_modal_count, NA_normalized_pronoun_count], ['OP',OP_normalized_contraction_count, OP_normalized_modal_count, OP_normalized_pronoun_count], ['SP', SP_normalized_contraction_count, SP_normalized_modal_count, SP_normalized_pronoun_count]]

os.chdir('../')
with open('Linguistics_Data.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
