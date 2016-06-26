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

def factorial(n):
	""" Return 1 * 2 * 3 * .... * n
	>>> factorial(0)
	1
	>>> factorial(1)
	1
	>>> factorial(3)
	6
	>>> factorial(6)
	720
	>>> factorial(8)
	40320
	"""
	i = 1
	result = 1
	while i <= n:
		result = result * i
		i += 1

	return result

def fib(n):
	"""Calculates the nth fibonacci numbers
	0, 1, 1, 2, 3, 5, 8, 13, 21, 34
	>>> fib(1)
	0
	>>> fib(2)
	1
	>>> fib(3)
	1
	>>> fib(6)
	5
	>>> fib(8)
	13
	>>> fib(10)
	34
	"""
	prev, curr = 0, 1
	i = 2
	while i <= n:
		prev, curr = curr, prev + curr
		i += 1

	return prev

def sum_naturals(n):
	"""Computes 1 + 2 + 3 + ... + n
	>>> sum_naturals(0)
	0
	>>> sum_naturals(1)
	1
	>>> sum_naturals(3)
	6
	>>> sum_naturals(10)
	55
	>>> sum_naturals(100)
	5050
	"""
	i = 1
	result = 0
	while i <= n:
		result = result + i
		i += 1
	return result

def b_sum_naturals(n):
	"""Computes 1 + 2 + 3 + ... + n
	>>> b_sum_naturals(3)
	6
	>>> b_sum_naturals(10)
	55
	>>> b_sum_naturals(100)
	5050
	"""
	return n * (n + 1) // 2



def is_prime(n):
	"""Returns true if a number is is_prime
	DIVISIBLE BY ONLY 1 AND n
	LOGIC : NUMBER IS DIVISIBLE BY A NUMBER BETWEEN 1
	AND N, THEN THE NUMBER IS NOT PRIME
	24
	2 - 23
	24
	1 * 24
	2 * 12
	3 * 8
	4 * 6
	169
	1 * 169
	13 * 13
	>>> is_prime(2)
	True
	>>> is_prime(3)
	True
	>>> is_prime(97)
	True
	>>> is_prime(24)
	False
	>>> is_prime(169)
	False
	"""
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def combine(left, right):
	""" Combines the digits on the left number
	with the digits on the right number
	123456 = 123 * 1000 + 456
	11220 = 112 * 100 + 20
	103 = 10 * 10 + 3
	>>> combine(123, 456)
	123456
	>>> combine(112, 20)
	11220
	>>> combine(10, 3)
	103
	""" 
	factor = 1
	n = right
	while n: # while n != 0
		n = n // 10
		factor = factor * 10
	return left * factor + right

def reverse(n):
	"""Reverses the number
	321 = 3 * 100 + 2 * 10 + 1 * 1
	43 = 4 * 10 + 3 * 1 
	>>> reverse(123)
	321
	>>> reverse(34)
	43
	>>> reverse(20)
	2
	>>> reverse(23456)
	65432
	"""
	factor = pow(10, length_digit(n) - 1)
	result = 0
	while n:
		last = n % 10
		result = last * factor + result 
		n = n // 10
		factor = factor // 10
	return result


def length_digit(n):
	"""Computes the number of digits in n
	>>> length_digit(123)
	3
	>>> length_digit(123456)
	6
	>>> length_digit(4)
	1
	"""
	count = 0
	while n:
		n = n // 10
		count += 1
	return count




def longest_increasing_suffix(n):
	"""
	Return the longest increasing suffix of a positive integer n.
	last - 4
	suffix - 4
	
	#2nd iteration
	# some variable = 4
	k - 10
	last - 3
	suffix - 34
	>>> longest_increasing_suffix(63134)
	134
	>>> longest_increasing_suffix(233)
	3
	>>> longest_increasing_suffix(5689)
	5689
	>>> longest_increasing_suffix(568901)
	1
	"""
	m, suffix, k = 10 , 0, 1
	while n:
		n, last = n // 10, n % 10
		if last < m:
			m, suffix, k = last, last * k + suffix,  10 * k			
		else:
			return suffix
	return suffix

