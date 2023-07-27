#!/usr/bin/env python3
import sys
import csv
import string

# remove punctuation from a given word
def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    # looping over the words array and printing the word
    # with the count of 1 to the STDOUT after removing punctuation
    for word in words:
        cleaned_word = remove_punctuation(word)
        # write the results to STDOUT (standard output);
        # use '\t' as the separator between word and count
        print('%s\t%s' % (cleaned_word, 1))

