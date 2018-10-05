""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def h(n):
        def g(x):
            i = 1
            while i <= n:
                if i % 3 == 0:
                    x = f3(x)
                if i % 3 == 1:
                    x = f1(x)
                if i % 3 == 2:
                    x = f2(x)
                i = i + 1
            return x
        return g
    return h



## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10 + 10 * y
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n in (1,2):
        return n
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i < 2:
            return True
        if n % i == 0:
            return False
        return helper(i - 1)
    return helper (n // 2)

def interleaved_sum1(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def helper(term0,term1,k):
        if k == n:
            return term0(k)

        else:
            return term0(k) + helper(term1,term0,k + 1)
    return helper(odd_term,even_term,1)  


def interleaved_sum2(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def helper(k,term):
        if k > n:
            return 0
        else:
            return term(k) + helper(k + 2,term)
    return helper(1,odd_term) +helper(0,even_term)
 
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum2(5, lambda x: x, lambda x: x*x)
    29
    """
    total, term0, term1 = interleaved_helper(n, odd_term, even_term)
    return total

def interleaved_helper(n, odd_term, even_term):
    if n == 1:
        return odd_term(1), even_term, odd_term
    else:
        total, term0, term1 = interleaved_helper(n-1, odd_term, even_term)
        return total + term0(n), term1, term0


    


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"



    def helper(digit,k):
        if not k:
            return 0
        if k % 10 == digit :
            return 1 + helper(digit, k // 10)
        else:
            return helper(digit, k // 10)

    total = 0
    while n:
        last = n % 10
        n //= 10
        total += helper(10 - last,n)
    return total

