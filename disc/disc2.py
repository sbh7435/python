def count_stairs(n,k):
    """
    I want to go up a flight of stairs that has n steps.
    I can either take 1 or 2 or 3... or k steps each time.
    How many different ways can I go up this flight of stairs?

    >>> count_k(3, 3)   # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        i = 1
        total = 0
        while i <= k:
            total += count_stairs(n - i, k)
            i += 1
        return total
    