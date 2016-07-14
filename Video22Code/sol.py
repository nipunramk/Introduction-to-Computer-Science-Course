def evenify(n):
	if n % 2 == 1:
		return n + 1
	return n

def foo(n):
	"""Find the runtime of foo(evenify(n))"""
	if n < 1:
		return 2
	elif n % 2 == 0:
		return foo(n - 1) + foo(n - 2)
	else:
		return 1 + foo(n - 2)


class Link:
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest
	def __len__(self):
		return 1 + len(self.rest)
	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i - 1]
	def __repr__(self):
		rest_str = ''
		if self.rest is Link.empty:
			rest_str = ''
		else:
			rest_str = ', ' + repr(self.rest)
		return 'Link({0}{1})'.format(self.first, rest_str)
	def __iter__(self):
		return LinkIterator(self)
	
class LinkIterator:
	def __init__(self, link):
		self.link = link
		self.first = link.first
		
	def __next__(self):
		if self.link is Link.empty:
			self.current = self.first
			raise StopIteration
		result = self.link.first
		self.link = self.link.rest
		return result


def delete(link, elem):
	"""Deletes a the first instance of a
	particular element from a linked list
	>>> link1 = Link(1, Link(2, Link(3)))
	>>> delete(link1, 3)
	Link(1, Link(2))
	>>> link2 = Link(1)
	>>> delete(link2, 3) # elem not in linked list 
	Link(1)
	>>> link3 = Link(2, Link(4, Link(6, Link(8, Link(9)))))
	>>> delete(link3, 6)
	Link(2, Link(4, Link(8, Link(9))))
	"""
	if link is Link.empty:
		return link
	elif link.first == elem:
		return link.rest
	else:
		return Link(link.first, delete(link.rest, elem))



def reverse(link):
	"""Returns a reversed version of the linked list
	>>> link1 = Link(1, Link(2, Link(3)))
	>>> reverse(link1)
	Link(3, Link(2, Link(1)))
	>>> link2 = Link(1)
	>>> reverse(link2)
	Link(1)
	>>> reverse(Link.empty)
	()
	>>> link3 = Link(2, Link(4, Link(6, Link(8, Link(9)))))
	>>> reverse(link3)
	Link(9, Link(8, Link(6, Link(4, Link(2)))))
	"""
	reversed = Link.empty
	while link != Link.empty:
		reversed = Link(link.first, reversed)
		link = link.rest
	return reversed

def has_cycle(link):
	"""
	Determines if a link list has a cycle
	>>> link1 = Link(1, Link(2, Link(3)))
	>>> has_cycle(link1)
	False
	>>> link1.rest.rest = link1 # Creates a cycle
	>>> has_cycle(link1)
	True
	>>> link2 = Link(2, Link(4, Link(6, Link(8, Link(9)))))
	>>> has_cycle(link2)
	False
	>>> link2.rest.rest.rest = link2.rest # Creates a cycle
	>>> has_cycle(link2)
	True
	"""

	if link is Link.empty or link.rest is Link.empty:
		return False
	slow = link
	fast = link
	while fast is not Link.empty and fast.rest is not Link.empty:
		slow = slow.rest
		fast = slow.rest.rest			
		if slow is fast:
			return True

	return False

class Tree:
	def __init__(self, entry, branches=[]):
		self.entry = entry
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = branches
	def __repr__(self):
		if not self.branches:
			branches_str = ''
		else:
			branches_str = ', ' + repr(self.branches)
		return 'Tree({0}{1})'.format(self.entry, branches_str)

def is_leaf(t):
	"""Returns true if tree t is a leaf and
	false otherwise
	>>> t1 = Tree(1, [Tree(2), Tree(3)])
	>>> is_leaf(t1)
	False
	>>> is_leaf(t1.branches[0])
	True
	"""
	return len(t.branches) == 0

def contains(elem, t):
	"""
	>>> t1 = Tree(1, [Tree(2), Tree(3)])
	>>> contains(4, t1)
	False
	>>> contains(2, t1)
	True
	>>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5), Tree(6)])
	>>> contains(4, t2)
	True
	"""
	if t.entry == elem:
		return True
	elif is_leaf(t):
		return False
	else:
		return True in [contains(elem, st) for st in t.branches]

def one(b):
	"""Returns 1 if b is a true value, 0 if false value"""
	if b:
		return 1
	else:
		return 0
def path_counter(t, n):
	"""Returns the number of paths in t 
	that have a sum larger than or equal to n
	*Hint use the one function to your advantage
	>>> t = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
	>>> path_counter(t, 3)
	3
	>>> path_counter(t, 6)
	2
	>>> path_counter(t, 9)
	1
	"""
	if is_leaf(t):
		return one(t.entry >= n)
	else:
		return sum([path_counter(st, n - t.entry) for st in t.branches])
