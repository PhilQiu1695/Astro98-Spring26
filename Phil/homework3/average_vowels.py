# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.
def counting_vowels_and_consonants(passage):
    num_vowel, num_consonant = 0, 0
    for l in passage:
        l = l.lower()
        if l.isalpha() and (l == "a" or l == "e" or l == "i" or l == "o" or l == "u"):
            num_vowel += 1
        elif l.isalpha():
            num_consonant += 1
    return (num_vowel, num_consonant)

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(para):
    num_sentences = 0
    for i in para:
        if i.isupper():
            num_sentences += 1
    num_vowel, num_consonant = counting_vowels_and_consonants(para)[0], counting_vowels_and_consonants(para)[1]
    avg_vowel, avg_consonant = num_vowel / num_sentences, num_consonant / num_sentences
    return (num_sentences, avg_vowel, avg_consonant)

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
print(f"The average vowels per sentence of the paragraph is {average_vowels_and_consonants(paragraph)[1]}. The average vowels per sentence of the paragraph is {average_vowels_and_consonants(paragraph)[2]}." )