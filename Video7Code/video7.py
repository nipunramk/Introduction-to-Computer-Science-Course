def summation(n, term): # bound to particular functions that define what we are summing
	i = 1
	result = 0
	while i <= n:
		result = result + term(i)
		i += 1
	return result


def square(x):
	return x * x

def cube(x):
	return x * x * x

def identity(x):
	return x

def make_adder(n):
	"""
	>>> add_three = make_adder(3)
	>>> add_three(5)
	8
	>>> add_three(10)
	13
	"""
	def adder(k):
		return n + k
	return adder

def sqrt_newton(a):
	"""a - intitial number we are trying to find the sqrt of
	x - initial estimate of the sqrt(a) - this is what we need to improve upon
	"""
	def sqrt_update(x):
		return 0.5 * (x + a / x)
	def sqrt_close(x):
		return approx_eq(x * x, a)
	return improve(sqrt_update, sqrt_close)

def improve(update, close, guess = 1):
	""" update - function that updates the sqrt (sqrt_update)
	close - function that returns True if the estimate is good enough (sqrt_close)
	guess - current estimate
	"""
	while not close(guess):
		guess = update(guess)
	return guess



def approx_eq(x, y, tolerance = 0.000001):
	"""x - estimate (x * x)
	y - actual value (a)
	"""
	return abs(x - y) < tolerance









