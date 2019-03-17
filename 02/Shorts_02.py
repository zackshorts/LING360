import re

# Gerunds: verbs acting as nouns ( Hiking is fun )
# Agent nouns: nouns that end in -or, -er and are derived from verbs ( actor, teacher )
# Recipient nouns: Suffix -ee is used as an indicator of passive party in transaction ( payee, employee )
# Other suffixes that transform verbs into nouns are: -tion, -sion, -ment, -ence, and -ance ( information, collision )


# Here is the text that we are going to extract the nominalized verbs from.
text = 'Farmer Jones met Jane when he was just a young man. He couldn\’t help falling in love with her immediately and asked her to marry him. She said yes although she knew it would mean getting up early to milk the cows for the rest of her life. “Love means never having to get up early to milk the cows”, said Farmer Jones, and explained that he would continue getting up early to milk the cows so Jane could sleep late every day. Everything went well until they tried to increase their profits by buying some chickens. The first night, a fox ate one of the chickens. Farmer Jones decided to build a fence to protect the chickens. But the ground was too hard so he couldn’t. He tried to use an axe to break the ground but it was much too hard. So he went to the local shop and tried to buy a gun. But he didn’t have any identification so he couldn’t buy one. He tried to borrow one from his neighbours but they were all worried about the fox too.“I regret not buying one when I had those rabbit problems”, he told Jane. So Jane went to the shop and bought a gun. That night she tried to stop the fox. At first she tried to scare the fox by shooting into the air but it didn’t work. So she tried to hit the fox but she missed. She called her husband and he ran after the fox to try catch it but he wasn’t fast enough. They tried shouting at the fox and they tried throwing things at it and they tried leaving other food for the fox but nothing worked. Soon they had only 1 chicken left. They tried asking their neighbours for help and one of their neighbours told them to try putting tiger dung on the ground. So they went to the local zoo to try to buy some tiger dung.They put the dung on the ground and they never saw the fox again. Employee, investigation, collision, acceptance,'


########################################################################
#####################     EXPLAINING THE REGEX     #####################
########################################################################
# (?!everything|nothing)\b\w+ing\b will match full words that end in 'ing' and are not "everything" or "nothing"

# (?!her|for|tiger|other|never|after)\b\w+[oe]r\b will match full words that end in 'er' or 'or' and are not
#     "her", "for", "tiger", "other", "never", "after"

# \b\w+ee\b matches full words that end in 'ee'

# (?!fence)\b\w+[ae]nce\b matches full words that end in 'ance' or 'ence' and are not "Fence"

# \b\w*[st]ion\b matches full words that end in 'ion'

results = re.findall(r'((?!everything|nothing)\b\w+ing\b|(?!her|for|tiger|other|never|after)\b\w+[oe]r\b|\b\w+ee\b|(?!fence)\b\w+[ae]nce\b|\b\w*[st]ion\b)', text, flags=re.I)

print(len(results))
print(results)
