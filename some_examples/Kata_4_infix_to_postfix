'''Original Kata here: https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python'''

from collections import deque
 
    
def prec(c):
    '''calculate weight for operators'''
    if c in '*/': return 3
    if c in '+-': return 4
    if c == '&': return 8
    if c == '^': return 2
    if c == '|': return 10
    return 100  # для открывающей скобки '('
 

def isOperand(c):
    '''check for name spaces and numbers'''
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
 
def to_postfix(infix):
    '''convert infix to postfix'''
    print(infix)
    if not infix or not len(infix):
        return True
    # создает пустой stack для хранения операторов
    s = deque()
    # создать строку для хранения постфиксного выражения
    postfix = ''
    check = False
    # обрабатывает инфиксное выражение слева направо
    for c in infix:
        # Случай 1. Если текущая лексема является открывающей скобкой '(', поместите ее в
        # stack
        if c == '(':
            check = True
            s.append(c)
        # Случай 2. Если текущая лексема является закрывающей скобкой ')'
        elif c == ')':
            check = False
            # извлекает токены из stack до тех пор, пока не появится соответствующая открывающая скобка '('
            # удален. Добавляйте каждый оператор в конец постфиксного выражения
            while s[-1] != '(':
                postfix += s.pop()
            s.pop()
        # Случай 3. Если текущая лексема является операндом, добавьте ее в конец
        # Постфиксное выражение
        elif isOperand(c):
            postfix += c
            print(postfix)
        # Случай 4. Если текущий токен является оператором
        else:
            # удаляет из stack операторы с более высоким или равным приоритетом
            # и добавьте их в конце постфиксного выражения.
            while s and prec(c) >= prec(s[-1]) and c != '^' or\
            s and prec(c) > prec(s[-1]) and c == '^' :
                postfix += s.pop()
            #, наконец, поместите текущий оператор на вершину stack
            s.append(c)
    # добавляет все оставшиеся операторы в stack в конце постфиксного выражения.
    while s:
        postfix += s.pop()

    return ''.join(postfix)
