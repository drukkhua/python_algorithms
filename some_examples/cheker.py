'''Aleksieiev Valentyn, 30/06/2022
Library with 2 new functions for check variables types in input console
'''

def input_variable(func, var_num, mes):
    '''func - from function variable_check
var_num - from function variable_check
mes - from function variable_check'''
    try:
        values = [func(input(f'{mes} #{i}: ')) for i in range(1, var_num + 1)]
    except Exception:
        print(f'You can input only {func.__name__} numbers\n')
        return input_variable(func, var_num, mes)
    return (values[0], values)[var_num > 1]

def variable_check(func=int, var_num=2, mes='Input variable'):
    '''func - input type for check, default = int
var_num - number of cariables, default = 2
mes - messege to print in input, default = 'Input variable'''
    values = []
    while not values and len(values)!=var_num:
        values = input_variable(func, var_num, mes)
        return values
