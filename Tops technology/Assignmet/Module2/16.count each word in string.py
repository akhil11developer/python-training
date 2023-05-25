"""
Write a Python program to count the occurrences of each word in a
given sentence
"""

sentence = "python is high level prgramming language , python language like to people."

# Split the sentence into a list of words

words = sentence.split()

# Create an empty dictionary to store the word counts

word_counts = {}

# Iterate through the list of words

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
         word_counts[word] += 1

print(word_counts)