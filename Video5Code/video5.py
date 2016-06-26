def square(x):
	"""Returns the square of a number
	>>> square(5)
	25
	>>> square(10)
	100
	>>> square(-7)
	49
	>>> square(0)
	0

	"""


	return x * x

def cube(x):
	"""Returns the cube of a number
	>>> cube(3)
	27
	>>> cube(10)
	1000
	>>> cube(-7)
	-343
	>>> cube(0)
	0
	"""
	return pow(x, 3)

def weight(mass, g = 9.8):
	"""Returns the weight of an object (mass * g)
	g - acceleration of gravity
	>>> weight(10)
	98.0
	>>> weight(5)
	49.0
	>>> weight(10, 12.0)
	120.0
	"""

	return mass * g

def middle(a, b, c):
	"""Returns the middle value in a set of three numbers
	>>> middle(3, 4, 5)
	4
	>>> middle(-2, -10, 10)
	-2
	>>> middle(-10, 3, -1)
	-1
	"""
	if b > a and b < c or b < a and b > c:
		return b
	elif a > b and a < c or a <b and a > c:
		return a
	else: 
		return c




































# def longest_increasing_suffix(n):
# 	"""
# 	Return the longest increasing suffix of a positive integer n.
# 	>>> longest_increasing_suffix(63134)
# 	134
# 	>>> longest_increasing_suffix(233)
# 	3
# 	>>> longest_increasing_suffix(5689)
# 	5689
# 	>>> longest_increasing_suffix(568901)
# 	1
# 	"""
# 	m, suffix, k = 10 , 0, 1
# 	while n:
# 		n, last = __________, n % 10
# 		if _________________:
# 			m, suffix, k = ___________, _________________,  10 * k			
# 		else:
# 			return suffix
# 	return suffix

# def differs_by_one_digit(m, n):
# 	"""Returns True if and only if m and n have the same number of digits,
# 	and they differ by exactly one digit.

# 	You may assume m and n are positive integers

# 	>>> differs_by_one_digit(3467, 3427) # 3rd digit differs 
# 	True
# 	>>> differs_by_one_digit(2013, 2011) # Last digit differs
# 	True
# 	>>> differs_by_one_digit(5, 2) # Only digit differs
# 	True
# 	>>> differs_by_one_digit(2013, 2013) # No digit differs 
# 	False
# 	>>> differs_by_one_digit(1013, 2011) # Both first and last differ 
# 	False
# 	>>> differs_by_one_digit(3102, 2013) # All digits differ 
# 	False
# 	>>> differs_by_one_digit(1, 21) # Different digit count
# 	False
# 	>>> differs_by_one_digit(21, 1) # Different digit count 
# 	False
# 	"""

# 	diffs = 0
# 	while m > 0:
		
# 		if __________________:
# 			return False
		
# 		m, t = m // 10, m % 10
# 		n, v = n // 10, n % 10

# 		if ___________:
# 			diffs = ______________
	
# 	return ____________


