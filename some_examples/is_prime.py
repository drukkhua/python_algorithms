'''Aleksieiev Valentyn
26/07/2022
Create the function is_prime, which takes 1 argument - a number from 0 to 1000,
and returns True if it is simple, and False - otherwise. 
'''
from cheker import variable_check


def isPrime(n):
#return true if n is prime or false if not
    if n < 0: return False
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0: return False
    return True

def naturals(n):
# выводит список простых чисел до n значения в виде списка
    primes = []    
    for i in range(2, n + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(i ** 0.5) + 1):
            if i % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)    
    return primes
    
while True:
    number = variable_check(int, 1, 'Number to determine is it prime or not')
    print(isPrime(number))
    if isPrime(number):
        [print(f'Natural nambers befor {number}: {num}') for num in naturals(number)]
    print('============CALCULATION FINISH============')
    if input('Press enter to validate new number "0" to exit: ') == '0': break
    
print('Thanks for testing my function isPrime & naturals! Have a nice day:)')