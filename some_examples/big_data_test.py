'''Aleksieiev Valentyn
22/07/2021
Программа найдет топ 15 повторяемых слов в летописи "Повести временных лет" и выведет
потраченное время двумя разными алгоритмами.'
Для справки в летописи около 65500 слов и порядка 400 тыс символов, буквы'.
'''

#test small text fragment
test_txt2 = '''Then hate me when thou wilt; if ever, now;
Now, while the world is bent my deeds to cross,
Join with the spite of fortune, make me bow,
And do not drop in for an after-loss:
Ah, do not, when my heart hath 'scoped this sorrow,
Come in the rearward of a conquer'd woe;
Give not a windy night a rainy morrow,
To linger out a purposed overthrow.
If thou wilt leave me, do not leave me last,
When other petty griefs have done their spite
But in the onset come; so shall I taste
At first the very worst of fortune's might, 

And other strains of woe, which now seem woe,
Compared with loss of thee will not seem so.
Then hate me when thou wilt; if ever, now;
Now, while the world is bent my deeds to cross,
Join with the spite of fortune, make me bow,
And do not drop in for an after-loss:
Ah, do not, when my heart hath 'scoped this sorrow,
Come in the rearward of a conquer'd woe;
Give not a windy night a rainy morrow,
To linger out a purposed overthrow.
If wilt leave me, do not leave me last,
When other petty griefs have done their
But in the onset come; so shall I taste
At first the very worst of fortune's might, 

And other strains of woe, which now seem woe,
Compared with loss of thee will not seem so.
Then hate me when thou wilt; if ever, now;
Now, while the world is bent my deeds to cross,
Join with the spite of fortune, make me bow,
And do not drop in for an after-loss:
Ah, do not, when my heart hath 'scoped this sorrow,
Come in the rearward of a conquer'd woe;
Give not a windy night a rainy morrow,
To linger out a purposed overthrow.
If thou wilt leave me, do not leave me last,
When other petty griefs have done their spite
But in the onset come; so shall I taste
At first the very worst of fortune's might, 

And other strains of woe, which now seem woe,
Compared with loss of thee will not seem so.'''
import re
from collections import Counter
import time


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """  
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        print(f'\033[1m{func.__name__} needs {time.perf_counter() - start_time:.5f} seconds\033[0m')
        return res
    return wrapper
    
@benchmark
def top_n_words(text, n):
    words = re.findall(r"\b[a-zа-я]+\b", text.lower()) 
    top_n = Counter(words).most_common(n)
    top = Counter(words)
    res = sum(count for w, count in Counter(words).most_common())
    print(f'\033[1mВсего слов в тексте: {res}\033[0m')
    return [tup for tup in top_n]

@benchmark
def txt_to_dict_print(txt, n=False):
    lst = re.findall(r"\b[a-zа-я]+\b", txt.lower())
    res_dic = {word: lst.count(word) for word in set(lst) if len(word)>0}
    res = sum(count for w, count in res_dic.items())
    print(f'\033[1mВсего слов в тексте: {res}\033[0m')
    n = (min(len(res_dic), n), len(res_dic))[n==0]
    return sorted(res_dic.items(), key=lambda x:x[1], reverse=True)[:n]    

print('Программа найдет топ 15 повторяемых слов в летописи "Повести временных лет" и выведет потраченное время двумя разными алгоритмами.')
print('Для справки в летописи около 65500 слов и порядка 400 тыс символов, буквы')
print('1. Функция top_n_words решают задачу через итератор Counter из модуля collection и выдаст первые 15 популярных слов')
print('2. Функция txt_to_dict_print решают задачу через генератор полного словаря из слов\nKey=Word, Value = count(Word) и также выведет 15 популярных слов из словаря\n')

#Читаем полностью повесть временных лет из файла!
with open('input-01.txt', 'r', encoding='utf-8') as file:
    txt_text_all = file.read()

#BIG DATA TEST
input('Press Enter to calculate BIG DATA TEST with 65k words: ')
[print(f'{word}: {count}', sep='\n')for word, count in top_n_words(txt_text_all, 15)]
print('========++++++BIG DATA TEST++++++==========')
[print(f'{word}: {count}', sep='\n')for word, count in txt_to_dict_print(txt_text_all, 15)]
print('==================================\n')    

#SMALL DATA TEST
input('Press Enter to calculate SMALL DATA TEST with 370 words: ')
[print(f'{word}: {count}', sep='\n')for word, count in top_n_words(test_txt2, 15)]
print('========++++++SMALL DATA TEST++++++==========')
[print(f'{word}: {count}', sep='\n')for word, count in txt_to_dict_print(test_txt2, 15)]
print('==================================\n')   

#USER DATA TEST
while True:
    txt = input('Input your sentence or a lot of the sentences here to calculate whiout or "0" to Exit: ')
    if txt == '0': break    
    #generate dict from list of tuples
    words_dict = {word: count for word, count in txt_to_dict_print(txt)}
    [print(f'{word}: {count}', sep='\n')for word, count in words_dict.items()]
    print('========++++++USER DATA TEST++++++==========\n')
    
        
