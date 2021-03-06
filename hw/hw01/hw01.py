from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a**2 + b**2 + c**2 - min(a,b,c)**2

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i = n // 2 + 1
    while i:
    	if n % i == 0:
    		return i
    	else :
    		i = i - 1
    return False

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())
    # here c(), t(), f() are evaluated before passing 
    # but in case of if-else they are not evaluated before

def c():
    "*** YOUR CODE HERE ***"
    return True

def t():
    "*** YOUR CODE HERE ***"
    return 1
def f():
    "*** YOUR CODE HERE ***"
    return 1 / 0  # causing error in with_if_fuction, but no error in with_if_statement..
    # Here we can also return f(), this would have caused infinite loop.. i.e.   return f()
    # In these both cases we are making both with_if_statement and with_if_function to do different things

    # or c() --> return False, t() --> return 1/0, f() --> return 1   :-> THIS IS ALSO A SOLUTION

def hailstone2(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    steps = 1
    while n != 1:
    	print(n)
    	if n % 2 == 0:
    		n = n // 2 # To prevent reaching at "1.0"
    	else :
    		n = 3 * n + 1
    	steps += 1
    print(n)
    return steps

def hailstone1(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    steps = 0
    while n:
    	print(n)
    	steps += 1
    	if n == 1:
    		return steps
    	if n % 2 == 0:
    		n = n // 2
    	else :
    		n = 3 * n + 1

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
    	return 1
    if n % 2 == 0:
    	return 1 + hailstone(n // 2)
    else :
    	return 1 + hailstone(3 * n + 1)
  