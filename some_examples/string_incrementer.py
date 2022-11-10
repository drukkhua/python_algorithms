"""
5kyu - https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""
def increment_num(num_str: str) -> str:
    '''resive a num like 200 and return  num + 1 + inverse 003
    or 990 -> 001 -> 100'''
    if not num_str: return '1'
    i = 0
    s = list(num_str)
    while i < len(s):
        if int(s[i]) < 9:
            s[i] = str( int(s[i])+1 )
            break
        else:  #if s[i] == 9
            s[i] = '0'
            if i == len(s) - 1:
                s += ['1']
                break
        i += 1
    return ''.join(s[::-1])
            

def increment_string(s):
    print(s)
    if not s: return '1'
   
    i = len(s) - 1
    stack_num = ''  #value of inverse num from the end of string
    while i>=0 and s[i].isnumeric():
        stack_num += s[i]
        i -= 1
    
    left_side = s[:i+1]

    
    return left_side + increment_num(stack_num)
