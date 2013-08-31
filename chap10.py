# Name: Aarthi Narayan

# 10.7

def is_anagram(s,t):
    x = list(s)
    y = list(t)
    x.sort()
    y.sort()
    return (x == y)

s = 'nba'
t = 'abc'
print is_anagram(s,t)

# 10.13

from bisect import *

def make_word_list():
    """Reads lines from a file and builds a list using append."""
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def in_bisect(word_list,word):
    i = bisect_left(word_list,word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def interlock(word_list, word):
    even = word[::2]
    odd = word[1::2]
    return in_bisect(word_list,even) and in_bisect(word_list,odd)

word_list = make_word_list()

for word in word_list:
    if interlock(word_list,word):
        print word, word[::2], word[1::2]

