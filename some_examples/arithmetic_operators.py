'''Aleksieiev Valentyn
22/07/2022
Create an arithmetic function that takes 3 arguments: the first 2 are numbers,
the third is the operation to be performed on them.
If the third argument is +, add them;
if -, then subtract;
* - multiply; / - divide (first to second).
In other cases, return the "Unknown operation" line.
'''
from operator import add, sub, mul, truediv, floordiv, pow, mod


MES = '''\nI can calculate any operation in this list:
+ : first + second
- : first - second
* : first * second
/: first / second (float)
//: first // second
**: first ** second
%:  first % second'''

# create dictionary of arithmetic functions as values and string operation as key
RULES = {'+': add, '-': sub, '*': mul, '/': truediv, '//': floordiv, '**': pow, '%': mod}

def arithmetics(a, b, op='+'):
    if op in RULES: return RULES[op](a, b)  #call func by using a dictionary value
    else: return "Unknown operation"
    
while True:
    print(MES)
    x, y, op = float(input('Input first value: ')), float(input('Input second value: ')), input('Input operator: ')
    print(f'{x} {op} {y} = {arithmetics(x, y, op)}')
    print('============CALCULATION FINISH============')   
    if input('Press enter to calculate new arithmetic operation or "0" to exit: ') == '0': break
    
print('Thanks for testing my function arithmetics! Have a nice day:)')