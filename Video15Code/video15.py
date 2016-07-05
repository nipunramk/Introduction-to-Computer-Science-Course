def sort(lst):
	"""Sort the given lst from least to greatest
	*** list length <= 1 ---> already sorted
	*** minimum item in list is always first	
	>>> sort([13, 4, 7, 10, 2, 5, 2, 1])
	[1, 2, 2, 4, 5, 7, 10, 13]
	"""
	if len(lst) <= 1:
		return lst
	minim = min(lst)
	lst.remove(minim)
	return [minim] + sort(lst)

def deep_map(f, lst):
	"""Map the function f over a list that
	(potentially) could be nested	
	length of list 0 --> return lst
	lst = [[1, 2], 3, [4]]
	lst[0] - [1, 2] <-- new lst
	[f(lst[0])] + deep_map(f, lst[1:]) --> [1, 4]
	>>> deep_map(lambda x: x + 1, [1, 2, 3, 4])
	[2, 3, 4, 5]
	>>> square = lambda x: x * x
	>>> deep_map(square, [[1, 2], 3, [4]])
	[[1, 4], 9, [16]]
	>>> deep_map(square, [[[3], 4, [5, 1]], 6])
	[[[9], 16, [25, 1]], 36]
	"""
	if len(lst) == 0:
		return lst
	elif type(lst[0]) != list:
		return [f(lst[0])] + deep_map(f, lst[1:])
	else: # list is nested - first element of the particular list is a list
		return [deep_map(f, lst[0])] + deep_map(f, lst[1:])

def is_anagram(s1, s2):
	"""Returns True is string s1 and string s2 are 
	anagrams of each other (note s1 and s2 don't need to be valid words)
	Anagram - word that can be formed by rearranging the letters of another
	>>> is_anagram('cinema', 'iceman')
	True
	>>> is_anagram('listen', 'silent')
	True
	>>> is_anagram('torchwood', 'doctorwho')
	True
	>>> is_anagram('grades', 'intelligent')
	False
	>>> is_anagram('smart', 'taser')
	False
	"""
	if len(s1) !=  len(s2):
		return False
	d = {}
	for letter in s1:
		if letter not in d:
			d[letter] = 1
		else:
			d[letter] += 1

	for char in s2:
		if char not in d:
			return False
		else:
			d[char] -= 1

	for key in d:
		if d[key] != 0:
			return False
	return True


def clever_is_anagram(s1, s2):
	"""Returns True is string s1 and string s2 are 
	anagrams of each other (note s1 and s2 don't need to be valid words)
	Anagram - word that can be formed by rearranging the letters of another
	>>> clever_is_anagram('cinema', 'iceman')
	True
	>>> clever_is_anagram('listen', 'silent')
	True
	>>> clever_is_anagram('torchwood', 'doctorwho')
	True
	>>> clever_is_anagram('grades', 'intelligent')
	False
	>>> clever_is_anagram('smart', 'taser')
	False
	"""
	return ''.join(sorted(s1)) == ''.join(sorted(s2))






	




