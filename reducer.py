#!/usr/bin/env python3
from operator import itemgetter
import sys

current_word = None
current_count = 0
# loop over the lines from STDIN (standard input)
for line in sys.stdin:
    # split line into word and count
    word, count = line.strip().split('\t')

    # convert count from string to integer
    try:
        count = int(count)
    except ValueError:
        # discard this line if count is not a number
        continue

    # if current word is the same as the previous word, add the count
    # if it's a new word, print the previous word and its count
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_word = word
        current_count = count

# print last word and its count
if current_word:
    print('%s\t%s' % (current_word, current_count))
