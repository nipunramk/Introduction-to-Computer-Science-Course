def remove(lst, element):
	"""Removes all instances of a particular 
	element from the list and returns a new list
	*Note, don't use the .remove(i) method 
	>>> remove([1, 2, 3, 4, 5], 3)
	[1, 2, 4, 5]
	>>> remove([2, 4, 5, 6, 8], 8)
	[2, 4, 5, 6]
	"""
	new_lst = []
	for item in lst:
		if item != element:
			new_lst.append(item)
	return new_lst


def remove_duplicates(lst):
	"""Returns a list with all duplicate elements
	removed from the list
	>>> remove_duplicates([1, 2, 2, 3, 4, 5, 6, 5, 3, 4, 4, 5, 6, 3, 4, 7, 1, 1, 2])
	[1, 2, 3, 4, 5, 6, 7]
	>>> remove_duplicates([2, 4, 5, 6])
	[2, 4, 5, 6]
	"""
	new_lst = []
	for elem in lst:
		if elem not in new_lst:
			new_lst.append(elem)

	return new_lst

	


def reverse(lst):
	"""Returns a reversed version of 
	the original list without using lst[::-1]
	>>> reverse([1, 2, 3, 4])
	[4, 3, 2, 1]
	>>> reverse([2])
	[2]
	>>> reverse([])
	[]
	"""
	new_lst = []
	index = len(lst) - 1
	while index >= 0:
		new_lst.append(lst[index])
		index -= 1
	return new_lst


	



def crazy_clear(lst):	
	"""Clear and return an empty list
	"""
	# for item in lst:
	# 	lst.remove(item)
	# return lst

	#^ THIS IS A TERRIBLE IDEA!!!!!!

	return []
	

def oddify(lst):
	"""Remove all elements that are even numbers
	>>> oddify([2, 3, 4, 5, 6])
	[3, 5]
	>>> oddify([1, 3, 5])
	[1, 3, 5]
	>>> oddify([4, 10, 2, 4, 6])
	[]
	"""
	copy = lst.copy()
	for item in copy:
		if item % 2 == 0:
			lst.remove(item)

	return lst
