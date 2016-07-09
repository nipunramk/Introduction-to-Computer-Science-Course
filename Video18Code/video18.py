def test_efficiency(n, elem):
	""" 
	Linear time function
	"""
	for i in range(n):
		if i == elem:
			return i
	return n

def factorial(n):
	"""
	1. figure out cost model
	input - 5
	fact(5) --> fact(4) -->fact(3) --> fact(2) ... fact(0) 6 calls
	input - 10
	fact(10), fact(9) ... fact(0) 11
	input -n
	n + 1
	This is a linear time function
		"""
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
def g(n):
	""" 
	cost model - bindings of i and j
	input -5
	i = 0 : j = 0, j =1, j= 2, .. j = 4 - 5 bindings
	i = 1: j = 0, j = 1, ... , j = 4 - 5 bindings
	...
	i = 4, j = 0, j =1, ... j = 4 - 5 bindings
	25 bindings
	input n
	n * n bindings
	This is a quadratic time function
	"""
	for i in range(n):
		for j in range(n):
			print("Hello!")

def h(n):
	""" 
	input - 5
	i = 0: j = 0 - done - 2 bindings
	input - 10
	i = 0: j =0 - done - 2 bindings
	input - n
	2 bindings
	This is a constant time function
	"""
	for i in range(n):
		for j in range(n):
			if i <= n:
				return i

def modular(n):
	""" 
	input - 5
	modular(5), modular(4), ... , modular(0) - 6 calls
	input- 10
	modular(10), modular(9) ... modular(7) - 4 calls
	modular(13), modular(12) ... modular(7) - 7 calls
	worse case - 7 calls
	This is a constant time function
	"""
	if n % 7 == 0:
		return n
	else:
		return modular(n - 1)

def function(n):
	"""
	cost model - bindings of n
	input - 8 
	n - 4, n - 2, n - 1, n - 0 - 4 bindings
	input - 32
	n - 16, n - 8, n - 4, n -2 , n- 1, n- 0 - 6 bindings
	n
	log2n + 1 
	This is a logarithmic time function
	"""
	count = 0
	while n < 1:
		count += 1
		n = n // 2
	return count

def f(n):
	"""
	Exponential time function 
	"""
	if n == 1:
		return n
	else:
		return f(n - 1) + f(n - 1)


def fib(n):
	"""
	Approximately exponential time function
	"""
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n - 2) + fib(n - 1)

def memo(f):
	"""A higher order function that returns a faster
	version of the tree recursive fibonacci - linear time function"""
	memory = {} # idea - map a key that's an argument of the fib function to it's computer result
	def memoized(n):
		if n not in memory:
			memory[n] = f(n)
		return memory[n]

	return memoized





	




	