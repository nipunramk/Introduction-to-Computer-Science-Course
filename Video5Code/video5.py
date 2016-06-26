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
