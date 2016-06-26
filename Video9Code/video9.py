def factorial(n):	
	i = 1
	result = 1
	while i <= n:
		result = result * i
		i += 1

	return result

def factorial_rec(n):
	"""
	>>> factorial_rec(1)
	1
	>>> factorial_rec(3)
	6
	>>> factorial_rec(8)
	40320
	"""
	
	return n * factorial_rec(n - 1)

def sum_digits_iter(n):
	result = 0
	while n:
		last = n % 10
		n, result = n // 10, result + last
	return result

def sum_digits_rec(n):
	"""
	123 = 12, 3
	3452 = 345, 2
	sum(3452) = sum(345) + 2
	>>> sum_digits_rec(4)
	4
	>>> sum_digits_rec(123)
	6
	>>> sum_digits_rec(3452)
	14
	"""
	if n < 10:
		return n
	else:
		all_but_last, last = n // 10, n % 10
		return sum_digits_rec(all_but_last) + last

