from doctest import testmod,run_docstring_examples

def split(n):
    return n // 10 , n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    """ Return the luhn's sum of a no
    >>> luhn_sum(2)
    2
    >>> luhn_sum(12)
    4
    >>> luhn_sum(42)
    10
    >>> luhn_sum(138743)
    30
    >>> luhn_sum(5105105105105100) # example Mastercard
    20
    >>> luhn_sum(4012888888881881) # example Visa
    90
    >>> luhn_sum(79927398713) # from Wikipedia
    70
    """
    
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    if n < 10:
        return sum_digits(2 * last)
    else:
        return luhn_sum(all_but_last) + sum_digits(2 * last)

print(luhn_sum(79927398713))

def valid_card(card_no):
    """ Return True or False using luhn's sum for a card
    >>> valid_card(2)
    False
    >>> valid_card(12)
    False
    >>> valid_card(42)
    True
    >>> valid_card(138743)
    True
    >>> valid_card(5105105105105100) # example Mastercard
    True
    >>> valid_card(4012888888881881) # example Visa
    True
    >>> valid_card(79927398713) # from Wikipedia
    True
    """
    if not luhn_sum(card_no) % 10:
        return True
    else:
        return False
        
print(valid_card(79927398713))

print(testmod())