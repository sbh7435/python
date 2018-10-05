""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if max(a,b) % min(a,b) == 0:
    	return min(a,b)
    else:
    	return gcd(min(a,b), max(a,b) % min(a,b))

def hailstone1(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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
    
    def helper(n, count):
    	print(n)
    	if n == 1:
    		return count
    	if n % 2 == 0:
    		return helper(n // 2, count + 1)
    	else:
    		return helper(3 * n + 1, count + 1)
    return helper(n, 1)