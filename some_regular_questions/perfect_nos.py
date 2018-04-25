def keep_if(filter_fn,seq):
	"""
	apply filter_fn on each element in the sequence and keeps which passes the filter function
	"""
	return [x for x in seq if filter_fn(x)]

def divisors(n):
	divides_n = lambda x: n % x == 0
	# return keep_if(divides_n,range(1,n))			note --> this returns [] for n = 1
	return keep_if(divides_n,range(1,(n // 2) + 2))

def perfect(n):
	is_perfect = lambda x: sum(divisors(x)) == x
	return keep_if(is_perfect,range(1,n))

""" Note perfect is made on divisors and is_perfect and keep_if; divisors is made on divides_n and keep_if

"""