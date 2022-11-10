"""
One of the first chain emails I ever received was about a supposed Cambridge University study that suggests your brain can
read words no matter what order the letters are in, as long as the first and last letters of each word are correct.

Your task is to create a function that can take any string and randomly jumble the letters within each word while leaving
the first and last letters of the word in place.

For example,

mixwords('Winter is coming') // returns 'Wntier is cminog' or 'Wtiner is conimg'
mixwords('Hey, friends!') // returns 'Hey, fierdns!' or 'Hey, fernids!'
"""
import re
from random import shuffle


def mix_words(s):
    if not s: return 'undefined'
    
    lst = re.split(r'\b', s)

    for i, word in enumerate(lst):
        if len(word)>3:
            new_word = list(word[1:-1])
            while new_word == list(word[1:-1]):
                shuffle(new_word)
            
            lst[i] = word[0] + ''.join( new_word ) + word[-1]
    
    return ''.join(lst)
