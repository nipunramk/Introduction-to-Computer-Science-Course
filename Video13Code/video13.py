def is_substring(sub, string):
	"""
	>>> is_substring('race', 'race car')
	True
	>>> is_substring('noon', 'afternoon')
	True
	>>> is_substring('here', "Where's my food?")
	True
	>>> is_substring('yolo', 'death')
	False
	"""
	return sub in string
	
	

def is_palindrome(s1):
	"""
	>>> is_palindrome('racecar')
	True
	>>> is_palindrome('tent')
	False
	"""
	return s1[::-1] == s1

def check_repeated(s):
	"""Returns true if a string has repeated characters
	false otherwise
	>>> check_repeated('hello')
	True
	>>> check_repeated('unique')
	True
	>>> check_repeated("don't have")
	False
	"""
	if len(s) <= 1:
		return False
	pivot = s[0]
	for char in s[1:]:
		if char == pivot:
			return True
	return check_repeated(s[1:])
	




def make_list(n):
	"""Makes a list containing integers
	from 1 to n"""
	return list(range(1, n + 1))
	

def sum_naturals(n):
	"""1 + 2 + 3 + ... + n
	>>> sum_naturals(10)
	55
	>>> sum_naturals(1)
	1
	>>> sum_naturals(100)
	5050
	"""
	result = 0
	for i in range(n + 1):
		result += i
	return result
	

def reverse(lst):
	"""Reverse a list without a return statement
	and without using lst[::-1]
	1 --> 1
	1 2 3 --> 3 2 1
	1 2 3 4 --> 4 3 2 1
	1 2 3 4 5 6 --> 6 5 4 3 2 1
	1 <--> 6 (0th and 5th)
	2 <--> 5 (1st and 4th)
	3 <--> 4 (2nd and 3rd)
	a (kth index and length - 1 - kth index)

	"""
	n = len(lst)
	for k in range(n // 2):
		lst[k], lst[n - 1 -k] = lst[n - 1 - k], lst[k]
	

def character_tracker(word, letter):
	"""Returns the number of times a letter
	occurs in a word
	>>> character_tracker('hello', 'l')
	2
	>>> character_tracker('numbers', 's')
	1
	>>> character_tracker('nothing', 'w')
	0
	"""
	if letter not in word:
		return 0
	tracker = {}
	for char in word:
		if char in tracker:
			tracker[char] += 1
		else:
			tracker[char] = 1
	return tracker[letter]
	



