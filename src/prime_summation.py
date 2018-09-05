"""
Summation of primes kata.
"""
import sys


def O_n_squared_summationOfPrimes(primes):
    """
    return the sum of primes of a number.
    """
    prime_sum = 0
    for number in range(2, primes + 1):
        mod_zero = False
        for digit in range(2, number + 1):
            if digit == number and mod_zero is False:
                prime_sum += number
            elif number % digit == 0:
                mod_zero = True

    return prime_sum


def summationOfPrimes(primes):
    """
    """
    x = range(2, primes + 1)
    

if __name__ == '__main__':
    x = int(sys.argv[1])
    phrase = f'Summation of primes of {x} is {summationOfPrimes(x)}'
    print(phrase)
