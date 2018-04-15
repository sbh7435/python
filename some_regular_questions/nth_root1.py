from math import pow
from operator import mul
def n_update(f,df):
	""" returns a function to update the value of guess"""
	def h(x):
		return x-f(x)/df(x)
	return h

def tol(x,y,tol=1e-5):
	return abs(x-y)<tol

def improve(update,close,guess=1):
	while not close(guess):
		guess=update(guess)
	return guess

def nth_root(a,n):

	""" find the nth root of a number
	>>> nth_root(2,2)
	1.4142156862745099
	>>> nth_root(2,10)
	1.0717734687765739
	>>> nth_root(2,20)
	1.0352649319061498
	>>> nth_root(2,40)
	1.017479698486979
	>>> nth_root(2,100)
	1.0069555534056853

	"""

	def f(x):
		return pow(x,n)-a
	def df(x):
		return mul(n,pow(x,n-1))
	def close(x):
		return tol(f(x),0)
	return improve(n_update(f,df),close)

	
	