def is_even(n):
	if n == 0:
		return True
	else:
		return is_odd(n - 1)


def is_odd(n):
	if n == 0:
		return False
	else:
		return is_even(n - 1)

def sum_digits(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

def split(n):
	return n // 10, n % 10

def luhn_sum(n):
	"""Return the luhn sum of a number n
	*not going to double the last digit
	>>> luhn_sum(5)
	5
	>>> luhn_sum(12)
	4
	>>> luhn_sum(1827634)
	31
	>>> luhn_sum(5105105105105100)
	20
	"""
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return last + luhn_double(all_but_last)

def luhn_double(n):
	"""Return the luhn sum of a number n
	*doubles the last digit
	"""
	all_but_last, last = split(n)
	doubled = sum_digits(last * 2)
	if n < 10:
		return doubled
	else:
		return doubled + luhn_sum(all_but_last)


def fib_iter(n):
	prev, curr = 0, 1
	i = 2
	while i <= n:
		prev, curr = curr, prev + curr
		i += 1

	return prev

def fib(n):
	"""0, 1, 1, 2, 3, 5, 8, 13, 21, 34
	1 = 0 + 1
	8 = 3 + 5
	34 = 13 + 21
	fib(n) = fib(n - 2) + fib(n - 1)
	"""
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n - 2) + fib(n - 1)


def count_partition(n, m):
	"""	
	Two possibilities:
	use at least one m: n - m, m
	dont use m: n, m - 1
	>>> count_partition(5, 3)
	5
	>>> count_partition(6, 4)
	9
	"""
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		with_m = count_partition(n - m, m)
		without_m = count_partition(n, m - 1)
		return with_m + without_m
	


