# Ex 11.9

t = [1,2,1,3]

def has_duplicates(t):
    d = {}
    for s in t:
        if s in d:
            return True
        d[s] = True
    return False

print has_duplicates(t)

# Ex 11.10

def rotate_word(word,n):
    i = 0
    new_word = ""
    if len(word) > 0:
        while i < len(word):
            word_num=ord(word[i]) - ord('a')
            word_num = (word_num + n)  % 26 + ord('a')
            new_word=new_word + chr(word_num) 
            i = i + 1
        return new_word

def make_dict():
    fin = open('words.txt')
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = word
    return d

def rotate_pairs(word,word_dict):
    for i in range(1,14):
        rotated = rotate_word(word,i)
        if rotated in word_dict:
            print word, i , rotated  

word_dict = make_dict()
for word in word_dict:
    rotate_pairs(word,word_dict)


