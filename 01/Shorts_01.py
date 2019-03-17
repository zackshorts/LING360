# Zachary Shorts
# LING360
# Assignment 1 - Convert Singular to Plural


# This function will take the user input as a parameter and print the plural version of the word
def convert_to_plural(word):

    # save the lowercase version of the word
    converted_string = word.lower()

    # if the word ends in a y then change it to 'ies', do not include words that end in 'vowel + y' (such as boy, buy, bay)
    if converted_string[-1:] == 'y' and converted_string[-2:-1] not in ["a", "e", "i", "o", "u"]:
        converted_string = converted_string[:-1] + 'ies'

    # if the word ends in 'f' or 'fe' then change it to 'ves'
    elif converted_string[-1:] == 'f' or converted_string[-2:] == 'fe':
        index = converted_string.rfind('f')
        converted_string = converted_string[:index] + 'ves'

    # if the word ends in 'x', 's', 'z', 'o', 'ss', or 'ch' then add 'es' to the end
    elif converted_string[-1:] in ["x", "s", "z", "o"] or converted_string[-2:] == 'ss' or converted_string[-2:] == "ch":
        converted_string = converted_string + 'es'

    # if the word ends in 's' then add 'es' to the end
    elif converted_string[-1:] == 's':
        converted_string = converted_string + 'es'

    # if nothing else matches before this, then add 's' to the end
    else:
        converted_string = converted_string + 's'

    # print the old word and the new pluralized word
    print("\n" + word + " has been converted to " + converted_string + "\n\n\n")


# User Input Menu
# this keeps repeating until the user types quit
while True:
    # grabs word from user input
    word_to_convert = input("What word would you like to convert to plural? Enter quit to leave. ")

    # Quits the program if the user input is 'quit' or 'Quit'
    if word_to_convert == 'quit' or word_to_convert == 'Quit':
        print("Goodbye!")
        quit()

    # Runs this function if the user input is not 'quit' or 'Quit'
    convert_to_plural(word_to_convert)
