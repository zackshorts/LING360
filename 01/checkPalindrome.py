word1 = input("what is the word you want to check? ")
word1.lower()
word2 = word1

if word2 == word1[::-1]:
    print("yeah it is a palindrome")
else:
    print("nope it is not a palindrome")
