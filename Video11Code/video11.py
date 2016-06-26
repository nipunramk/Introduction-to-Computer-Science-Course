def cascade1(n):
	if n < 10:
		print(n)
	else:		
		cascade1(n // 10)
		print(n)



























def combine(left, right):
	factor = 1
	n = right
	while n: # while n != 0
		n = n // 10
		factor = factor * 10
	return left * factor + right

def reverse(n):
	"""Use the combine function to define reverse recursively
	*** For the sake of not dealing with annoying edge cases,
	assume that n does not contain any digits that are 0 ***

	FIRST STEP OF ANY RECURSIVE PROBLEM
	1. Analyze the simplest possible cases and find a solution to those
	2. These usually end up being base cases
	3. We are now going to work with examples and see
	 if we can find a larger pattern/recursive formulation

	 523 --> 325
	 last digit - n % 10
	 all but last - n // 10
	 last digit - 3
	 all but last - 52
	 *idea - last digit combined with reverse of all but last
	 combine(last, reverse(all but last))

	 123456 --> 654321

	>>> reverse(523)
	325
	>>> reverse(4)
	4
	>>> reverse(123456)
	654321
	"""
	if n < 10:
		return n
	else:
		return combine(n % 10, reverse(n // 10))








square = lambda x: x * x
double = lambda x: 2 * x

def memory(x, f):
	"""Returns a higher order function that prints its memories.

	AFTER FIRST LINE
	x - 3
	par_f - lambda x: x
	var_f - g

	AFTER SECOND LINE
	h - square
	----- print out 3
	var_f - we need this to be g
	par_f - square


	>>> f = memory(3, lambda x: x)
	>>> f = f(square)
	3
	>>> f = f(double)
	9
	>>> f = f(print)
	6
	>>> f = f(square)
	3
	None
	"""
	def g(h):
		print(f(x))
		return memory(x, h)
	return g





























def make_change(n):
	"""Function that finds the minimum number
	of coins necessary to make change for 
	a partcular n
	We have some special coins - 1 cent, 3 cent, and 4 cent
	n - non-negative integer
	
	>>> make_change(2)
	2
	>>> make_change(3) 
	1
	>>> make_change(5)
	2
	>>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
	2
	>>> make_change(7)
	2
	>>> make_change(21) # 4 cent * 5 + 1 cent
	6
	>>> make_change(30) # 4 cent * 6 + 3 cent * 2
	8
	"""
	if n < 1:
		return 0
	elif n < 3:
		return 1 + make_change(n - 1)
	elif n < 4: 
		use_1 = 1 + make_change(n - 1)
		use_3 = 1 + make_change(n - 3)
		return min(use_1, use_3)
	else:
		use_1 = 1 + make_change(n - 1)
		use_3 = 1 + make_change(n - 3)
		use_4 = 1 + make_change(n - 4)
		return min(use_1, use_3, use_4)
	
		


