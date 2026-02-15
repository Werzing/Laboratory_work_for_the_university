import random

def shuffle_words(s):
    words = s.split()
    random.shuffle(words)
    res = ""
    for w in words:
        res = res + w + " "
    return res.strip()

print(shuffle_words("яблоко груша апельсин банан"))