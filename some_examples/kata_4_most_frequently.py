'''original kata: https://www.codewars.com/kata/51e056fe544cf36c410000fb/'''

import re

def top_3_words(txt):
    allchgood = lambda str: all(ch in "'_:-?!" for ch in str) #if all char in word == "'" - return True
    txt = re.sub(r'[,.;\\/._:-?!-]', ' ', txt.lower())  #delete all special sibbols
    lst = txt.split(' ')  #split all word in the list
    
    #create a dic with word = key, count of words in txt = value
    res_dic = {word: lst.count(word) for word in set(lst) if len(word)>0 and not allchgood(word)}
    
    #sort dict reversed order in Values item
    res_dic = dict(sorted(res_dic.items(), key=lambda x:x[1], reverse=True))
    
    max_i = len(res_dic.keys()) 
    i = min(max_i+1, 3)
    
    #print result for check
    [print(f'{word}: {value}') for word, value in res_dic.items() if value > 1]
    
    return list(res_dic.keys())[:i]
