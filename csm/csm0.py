# Ques - 1 Write a HOF that passes the doctest Q ---> mystery
# challenge: write the fn body in one line   Q ---> mystery

def mystery(f, x):
	"""
	>>> from operator import add, mul
	>>> a = mystery(add, 3)
	>>> a(4) # add(3, 4)
	7
	>>> a(12)
	15
	>>> b = mystery(mul, 5)
	>>> b(7) # mul(5, 7)
	35
	>>> b(1)
	5
	>>> c = mystery(lambda x, y: x * x + y, 4)
	>>> c(5)
	21
	>>> c(7)
	23
	"""
	return lambda y: f(x,y)


# Ques - 3 Complete the definition of fox_says, which takes the three string parts of the fox’s
# statement (start, middle, and end) and a positive integer num indicating how many
# times to repeat middle. It returns a string.

# 	given: 
#	def fox_says(start, middle, end, num):
# 		"""
# 		>>> fox_says('wa', 'pa', 'pow', 3)
# 		'wa-pa-pa-pa-pow'
# 		>>> fox_says('fraka', 'kaka', 'kow', 4)
#		'fraka-kaka-kaka-kaka-kaka-kow'
#		"""
#		def repeat(k):
#
#
#
# 	return start + '-' + repeat(num) + '-' + end




def fox_says(start, middle, end, num):
"""
>>> fox_says('wa', 'pa', 'pow', 3)
'wa-pa-pa-pa-pow'
>>> fox_says('fraka', 'kaka', 'kow', 4)
'fraka-kaka-kaka-kaka-kaka-kow'
"""
def repeat(k):
	if k == 1:
		return middle
	return middle + '-' + repeat(n - 1)


return start + '-' + repeat(num) + '-' + end


#	Ques - 4 Fill in the blanks (without using any numbers in the first blank) such that the entire expression
# 	evaluates to 9.
#	(lambda x: lambda y: ________________)(_____)(lambda z: z*z)()

(lambda x: lambda y: y(x))(3)(lambda z: z*z)()




# Implement the combine function, which takes a nonnegative
# integer n, a two-argument function f, and a number result. It applies
# f to the first digit of n and the result of combining the rest of the digits of n by repeatedly
# applying f (see the doctests). If n has no digits (because it is zero), combine
# returns result.

#	def combine(n, f, result):
#	"""
#	Combine the digits in non-negative integer n using f.
#	>>> combine(3, mul, 2) # mul(3, 2)
#	6
#	>>> combine(43, mul, 2) # mul(4, mul(3, 2))
#	24
#	>>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3)
#	)))
#	16
#	>>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0))))
#	8
#	"""
#	if n == 0:
#	return result
#	else:
#return combine(_______ , _______ ,___________________)


def combine(n, f, result):
	"""
	Combine the digits in non-negative integer n using f.
	>>> combine(3, mul, 2) # mul(3, 2)
	6
	>>> combine(43, mul, 2) # mul(4, mul(3, 2))
	24
	>>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3)
	)))
	16
	>>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0))))
	8
	"""
	if n == 0:
	return result
	else:
	return combine( n // 10, f, f(n % 10 ,result))






# Today, the printers break down. Each time they are used, the first
# printer prints a random x copies 50 ≤ x ≤ 60, and the second printer prints a random
# y copies 130 ≤ y ≤ 140. James is satisfied as long as there’s at least 
# lower copies so there are enough for everyone, but no more than
# upper copies to prevent waste.


def sum_range(lower, upper):
	"""
	>>> sum_range(45, 60) # Printer 1 prints within this range
	True
	>>> sum_range(40, 55) # Printer 1 can print a number 56-60
	False
	>>> sum_range(170, 201) # Printer 1 + 2 will print between
	180 and 200 copies total
	True
	"""
	def copies(pmin, pmax):
		if lower <= pmin and pmax <= upper: 
			return True
		elif upper < pmin:
			return False
		return copies(pmin + 50, pmax + 60) or copies(pmin + 130, pmax + 140)
	return copies(0, 0)