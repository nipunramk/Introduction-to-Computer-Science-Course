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

def root(t):
	"""Returns the root of a tree
	>>> t1 = Tree(1, [Tree(2), Tree(3)])
	>>> root(t1)
	1
	>>> root(t1.branches[0])
	2
	>>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5), Tree(6)])
	>>> root(t2)
	1
	"""
	return t.entry

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

def sum_tree(t):
	"""Returns the sum of all the values in
	the tree
	>>> t1 = Tree(1, [Tree(2), Tree(3)])
	>>> sum_tree(t1)
	6
	>>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5), Tree(6)])
	>>> sum_tree(t2)
	21
	"""
	if is_leaf(t):
		return t.entry
	branches_sum = sum([sum_tree(branch) for branch in t.branches])
	return t.entry + branches_sum

def count_leaves(t):
	"""Returns the number of leaves in a tree
	>>> t1 = Tree(1, [Tree(2), Tree(3)])
	>>> count_leaves(t1)
	2
	>>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5), Tree(6)])
	>>> count_leaves(t2)
	4
	"""
	if is_leaf(t):
		return 1
	else:
		return sum([count_leaves(st) for st in t.branches])


def map_tree(f, t):
	"""Returns a new Tree that has every entry
	equal to the result of mapping a function f 
	over that entry
	>>> t1 = Tree(1, [Tree(2), Tree(3)])
	>>> map_tree(lambda x: x * x, t1)
	Tree(1, [Tree(4), Tree(9)])
	>>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5), Tree(6)])
	>>> map_tree(lambda x: x + 1, t2)
	Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6), Tree(7)])
	"""
	if is_leaf(t):
		return Tree(f(t.entry))
	else:
		return Tree(f(t.entry), [map_tree(f, st) for st in t.branches])

	