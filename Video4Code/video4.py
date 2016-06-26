def do_nothing():
	y = "nothing"

def pass_or_fail(grade):
	if grade >= 70:
		print("You Passed!")
	else:
		print("You failed :(")

def absolute_value(x):
	if x > 0:
		return x
	elif x == 0:
		return 0
	else:
		return -x

def is_positive(n):
	if n > 0:
		return True
	return False

def better_is_positive(n):
	return n > 0

def count_down(n):
	while n > 0:
		print(n)
		n -= 1 # n = n -1

def count_up(n):
	i = 1
	while i <= n:
		print(i)
		i += 1 # i = i + 1


