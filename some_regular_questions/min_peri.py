def peri(width, height):
	return 2 * (width + height)

def width(area,height):
	# assuming area is perfectly divided by height
	assert area % height == 0 , 'height is not a divisor of area'
	return area // height

def divisors(n):
	# divisors of 1 is 1, hence range(1, (n // 2) + 2)
	return [x for x in range(1,(n // 2)+ 2) if n % x == 0]

def min_peri(area):
	"""Returns min_peri given area, it considers all possible widths and heights in the range of area
	>>> min_peri(100)
	40
	"""
	possible_heights = divisors(area)
	return min(peri(width(area,h),h) for h in possible_heights)




# now find min peri in a range i.e. min peri when area = 1, 2, 3, 4, ..... n

def min_peri_in_range(n):
	"""
	>>> min_peri_in_range(10)
	[4, 6, 8, 8, 12, 10, 16, 12, 12]
	"""
	return [min_peri(x) for x in range(1,n)]