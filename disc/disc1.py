def keep_ints(cond,n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    >>> keep_ints(lambda x: x % 2 == 0,5)
    2
    4
    """
    k = 1
    while k <= n:
        if cond(k):
            print(k)
        k = k + 1






# Higher order version of keep_ints

def keep_ints(n):
    """
    >>> def is_even(x):
        return x % 2 == 0
    >>> keep_ints(7)(is_even)
    2
    4
    6
    >>> keep_ints(5)(lambda x: x % 2 == 0)
    2
    4
    """

    def f(cond):
        k = 1
        while k <= n:
            if cond(k):
                print(k)
            k += 1
    return f
