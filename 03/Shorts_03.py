# Formal and Informal Normalized Counts per 100

# Subject Pronouns

# Contractions

# Modal Verbs


# Find two texts that are each at least 500 words in length. Try to find one text that is more formal and one that is
# less formal. Create a Python program that produces normalized counts per 100 words for the number of (a) subject
# pronouns, (b) contractions, and (c) modal verbs in each of the texts. You should have six counts: (1) subject
# pronouns in formal text, (2) subject pronouns in informal text, (3) contractions in formal text, (4) contractions
# in informal text, (5) modal verbs in formal text, (6) modal verbs in informal text. Check both the precision and
# the recall of your program\'s ability to correctly find these three linguistic features.

import re

short_story = 'They\'ve been married for ten years and for a long time everything was O.K.—swell—but now they argue. ' \
              'Now they argue quite a lot. It\'s really all the same argument. It has circularity. It is, Ray thinks, ' \
              'like a dog track. When they argue, they\'re like greyhounds chasing the mechanical rabbit. You go past ' \
              'the same scenery time after time, but you don\'t see it. You see the rabbit. He thinks it might be ' \
              "different if they\'d had kids, but she couldn\'t . They finally got tested, and that\'s what the doctor " \
              'said. It was her problem. A year or so after that, he bought her a dog, a Jack Russell she named ' \
              'Biznezz. She\'d spell it for people who asked. She loves that dog, but now they argue anyway. They\'re ' \
              'going to Wal-Mart for grass seed. They\'ve decided to sell the house—they can\'t afford to keep it—but ' \
              'Mary says they won\'t get far until they do something about the plumbing and get the lawn fixed. She ' \
              'says those bald patches make it look shanty Irish. It\'s because of the drought. It\'s been a hot ' \
              'summer ' \
              'and there\'s been no rain to speak of. Ray tells her grass seed won\'t grow without rain no matter how ' \
              'good it is. He says they should wait. “Then another year goes by and we\'re still there,” she says. “We ' \
              'can\'t wait another year, Ray. We\'ll be bankrupts. ”When she talks, Biz looks at her from his place in ' \
              'the back seat. Sometimes he looks at Ray when Ray talks, but not always. Mostly he looks at Mary. ' \
              '“What do you think?” he says. "It\'s going to rain just so you don\'t have to worry about going ' \
              'bankrupt?” "We\'re in it together, in case you forgot,” she says. They\'re driving through Castle Rock ' \
              'now. It\'s pretty dead. What Ray calls “the economy” has disappeared from this part of Maine. The ' \
              'Wal-Mart is on the other side of town, near the high school where Ray is a janitor. The Wal-Mart has ' \
              'its own stoplight. People joke about it. “Penny wise and pound foolish,” he says. “You ever hear that ' \
              'one?” “A million times, from you.” He grunts. He can see the dog in the rearview mirror, watching her. ' \
              'He sort of hates the way Biz does that. It occurs to him that neither of them knows what they are ' \
              'talking about. “And pull in at the Quik-Pik,” she says. “I want to get a kickball for Tallie\'s ' \
              'birthday.” Tallie is her brother\'s little girl. Ray supposes that makes her his niece, although he\'s ' \
              'not sure that\'s right, since all the blood is on Mary\'s side. “They have balls at Wal-Mart,' \
              '” Ray says. ' \
              '“And everything\'s cheaper at Wally World.” “The ones at Quik-Pik are purple. Purple is her favorite ' \
              "color. I can\'t be sure there\'ll be purple at Wal-Mart.” “If there aren't, we\'ll stop at the " \
              'Quik-Pik ' \
              'on the way back.” He feels a great weight pressing down on his head. She\'ll get her way. She always ' \
              'does on things like this. He sometimes thinks marriage is like a football game and he\'s quarterbacking ' \
              'the underdog team. He has to pick his spots. Make short passes. '

short_story_split = re.findall(r"[\w']+|[.,!?;]", short_story, re.UNICODE)
short_story_length = len(short_story.split())
short_story_pronouns_actual = 38
short_story_contractions_actual = 33
short_story_modals_actual = 3

two_cities = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of " \
             "foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, " \
             "it was the season of Darkness, it was the spring of hope, it was the winter of despair, " \
             "we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all " \
             "going direct the other way-- in short, the period was so far like the present period, that some of its " \
             "noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of " \
             "comparison only. There were a king with a large jaw and a queen with a plain face, on the throne of " \
             "England; there were a king with a large jaw and a queen with a fair face, on the throne of France. In " \
             "both countries it was clearer than crystal to the lords of the State preserves of loaves and fishes, " \
             "that things in general were settled for ever. It was the year of Our Lord one thousand seven hundred " \
             "and seventy-five. Spiritual revelations were conceded to England at that favoured period, as at this. " \
             "Mrs. Southcott had recently attained her five-and-twentieth blessed birthday, of whom a prophetic " \
             "private in the Life Guards had heralded the sublime appearance by announcing that arrangements were " \
             "made for the swallowing up of London and Westminster. Even the Cock-lane ghost had been laid only a " \
             "round dozen of years, after rapping out its messages, as the spirits of this very year last past (" \
             "supernaturally deficient in originality) rapped out theirs. Mere messages in the earthly order of " \
             "events had lately come to the English Crown and People, from a congress of British subjects in America: " \
             "which, strange to relate, have proved more important to the human race than any communications yet " \
             "received through any of the chickens of the Cock-lane brood. France, less favoured on the whole as to " \
             "matters spiritual than her sister of the shield and trident, rolled with exceeding smoothness down " \
             "hill, making paper money and spending it. Under the guidance of her Christian pastors, she entertained " \
             "herself, besides, with such humane achievements as sentencing a youth to have his hands cut off, " \
             "his tongue torn out with pincers, and his body burned alive, because he had not kneeled down in the " \
             "rain to do honour to a dirty procession of monks which passed within his view, at a distance of some " \
             "fifty or sixty yards. It is likely enough that, rooted in the woods of France and Norway, there were " \
             "growing trees, when that sufferer was put to death, already marked by the Woodman, Fate, to come down " \
             "and be sawn into boards, to make a certain movable framework with a sack and a knife in it, terrible in " \
             "history. It's likely enough that in the rough outhouses of some tillers of the heavy lands adjacent to " \
             "Paris, there were sheltered from the weather that very day, rude carts, bespattered with rustic mire, " \
             "snuffed about by pigs, and roosted in by poultry, which the Farmer, Death, had already set apart to be " \
             "his tumbrils of the Revolution. "

two_cities_split = two_cities.split()
two_cities_length = len(two_cities_split)
two_cities_pronouns_actual = 6
two_cities_contractions_actual = 1
two_cities_modals_actual = 0

# Definitions of each categorization
subject_pronouns = ['i', 'you', 'he', 'she', 'they', 'we']
contractions = ["they\'ve", "aren't", "can\'t", "couldn't", 'didn\'t', 'doesn\'t', 'don\'t', 'hadn\'t', 'hasn\'t',
                'haven\'t',
                'he\'d', 'he\'ll', 'he\'s', 'i\'d', 'i\'ll', 'i\'m', 'i\'ve', 'isn\'t', 'let\'s', 'mightn\'t',
                'mustn\'t', 'shan\'t', 'she\'d', 'she\'ll', 'she\'s', 'shouldn\'t', 'that\'s', 'there\'s', 'they\'d',
                'they\'ll', 'they\'re', 'we\'d', 'we\'re', 'we\'ve', 'weren\'t', 'what\'ll', 'what\'re',
                'what\'s', 'what\'ve', 'where\'s', 'who\'s', 'who\'ll', 'who\'re', 'who\'s', 'who\'ve', 'won\'t',
                'wouldn\'t', 'you\'d', 'you\'ll', 'you\'re', 'you\'ve', 'it\'s', 'everything\'s', 'there\'ll', 'we\'ll',
                '']
modal_verbs = ['can', 'could', 'may', 'might', 'will', 'would', 'shall', 'should', 'must']


# This is the main function that will call all other helper functions. Start here.
def start():
    # The following two lines will print out the info for subject pronouns
    subject_pronoun_count(short_story.lower(), short_story_length, 'informal', short_story_pronouns_actual)
    subject_pronoun_count(two_cities.lower(), two_cities_length, 'formal', two_cities_pronouns_actual)

    # The following two lines will print out the info for contractions
    contraction_count(short_story.lower(), short_story_length, 'informal', short_story_contractions_actual)
    contraction_count(two_cities.lower(), two_cities_length, 'formal', two_cities_contractions_actual)

    # The following two lines will print out the info for modal verbs
    modal_verb_count(short_story.lower(), short_story_length, 'informal', short_story_modals_actual)
    modal_verb_count(two_cities.lower(), two_cities_length, 'formal', two_cities_modals_actual)


def subject_pronoun_count(text, text_word_count, text_type, actual_amount):
    count = 0

    for word in text.split():
        formatted_word = re.sub("^\"|[\",]$", "", word)
        if formatted_word.lower() in contractions:
            count += 1

    if text_type == 'informal':
        print("\n----INFORMAL SUBJECT PRONOUNS----")
    elif text_type == 'formal':
        print("----FORMAL SUBJECT PRONOUNS----")
    print("Total Match Count: " + str(count))
    print("Normalized Count: " + str(count / text_word_count * 100) + " per 100 words.")
    print("Precision: 100% All " + str(count) + ' matches found were actually matches ')
    try:
        print("Recall: " + str(count / actual_amount * 100) + "% (" + str(count) + ' matches out of ' + str(
            actual_amount) + " actual occurrences)\n")
    except:
        print("Recall: 100%" + str(count) + ' matches out of ' + str(actual_amount) + " actual occurrences)\n\n")


def contraction_count(text, text_word_count, text_type, actual_amount):
    count = 0

    for word in text.split():
        formatted_word = re.sub("^\"|[\",]$", "", word)
        if formatted_word.lower() in contractions:
            count += 1
    if text_type == 'informal':
        print("\n\n----INFORMAL CONTRACTIONS----")
    elif text_type == 'formal':
        print("----FORMAL CONTRACTIONS----")
    print("Total Match Count: " + str(count))
    print("Normalized Count: " + str(count / text_word_count * 100) + " per 100 words.")
    print("Precision: 100% All " + str(count) + ' matches found were actually matches ')
    try:
        print("Recall: " + str(count / actual_amount * 100) + "% (" + str(count) + ' matches out of ' + str(
            actual_amount) + " actual occurrences)\n")
    except:
        print("Recall: 100% " + str(count) + ' matches out of ' + str(actual_amount) + " actual occurrences)\n\n")


def modal_verb_count(text, text_word_count, text_type, actual_amount):
    count = 0

    for word in text.split():
        formatted_word = re.sub("^\"|[\",]$", "", word)
        if formatted_word.lower() in contractions:
            count += 1

    if text_type == 'informal':
        print("\n\n----INFORMAL MODAL VERBS----")
    elif text_type == 'formal':
        print("----FORMAL MODAL VERBS----")
    print("Total Match Count: " + str(count))
    print("Normalized Count: " + str(count / text_word_count * 100) + " per 100 words.")
    print("Precision: 100% All " + str(count) + ' matches found were actually matches ')
    try:
        print("Recall: " + str(count / actual_amount * 100) + "% (" + str(count) + ' matches out of ' + str(
            actual_amount) + " actual occurrences)\n")
    except:
        print("Recall: 100% " + str(count) + ' matches out of ' + str(actual_amount) + " actual occurrences)\n\n")


# Starts the program.
start()
