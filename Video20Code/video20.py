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


def length(link):
	"""Finds the length of a linked list
	>>> length(Link.empty)
	0
	>>> link1 = Link(1, Link(2, Link(3)))
	>>> length(link1)
	3
	>>> link2 = Link(1)
	>>> length(link2)
	1
	>>> link3 = Link(2, Link(4, Link(6, Link(8, Link(9)))))
	>>> length(link3)
	5
	"""
	count = 0
	while link is not Link.empty:
		count += 1
		link = link.rest

	return count



def length_rec(link):
	"""Finds the length of a linked list recursively
	>>> length_rec(Link.empty)
	0
	>>> link1 = Link(1, Link(2, Link(3)))
	>>> length_rec(link1)
	3
	>>> link2 = Link(1)
	>>> length_rec(link2)
	1
	>>> link3 = Link(2, Link(4, Link(6, Link(8, Link(9)))))
	>>> length_rec(link3)
	5
	"""
	if link is Link.empty:
		return 0
	else:
		return 1 + length_rec(link.rest)


def get(link, index):
	"""Gets an item at a particular index
	from a linked list
	>>> link1 = Link(1, Link(2, Link(3)))
	>>> link2 = Link(1)
	>>> link3 = Link(2, Link(4, Link(6, Link(8, Link(9)))))
	>>> get(link1, 2)
	3
	>>> get(link2, 0)
	1
	>>> get(link3, 3)
	8
	"""
	if index == 0:
		return link.first
	else:
		return get(link.rest, index - 1)



def print_link(link):
	"""Prints the link as such
	>>> link = Link(1, Link(2, Link(3)))
	>>> print_link(link)
	1 2 3 
	>>> print_link(Link.empty)	
	>>> print_link(link.rest)
	2 3 
	"""
	if link is Link.empty:
		return
	s = ''
	while link is not Link.empty:
		s = s + str(link.first) + ' '
		link = link.rest
	print(s)




def insert(link, item, index):
	"""Inserts an item at a particular index
	and returns a new linked list
	* Assume a valid index is given for simplicity 
	(0 <= index < length(link))
	>>> link1 = Link(1, Link(2, Link(3)))
	>>> insert(link1, 4, 2)
	Link(1, Link(2, Link(4, Link(3))))
	>>> link2 = Link(2, Link(4, Link(6, Link(8, Link(9)))))
	>>> insert(link2, 10, 0)
	Link(10, Link(2, Link(4, Link(6, Link(8, Link(9))))))
	"""
	if index == 0:
		return Link(item, link)
	else:
		return Link(link.first, insert(link.rest, item, index - 1))



def insert_mut(link, item, index):
	"""Mutates a link by inserting an item
	into the appropriate index. Does not return
	a new linked list
	*Note: assume index is in range for simplicity, 
	also assume that Link.empty is not passed in as link
	>>> link1 = Link(1, Link(2, Link(3)))
	>>> insert_mut(link1, 4, 2)
	>>> link1
	Link(1, Link(2, Link(4, Link(3))))
	>>> link2 = Link(2, Link(4, Link(6, Link(8, Link(9)))))
	>>> insert_mut(link2, 10, 0)
	>>> link2
	Link(10, Link(2, Link(4, Link(6, Link(8, Link(9))))))
	"""
	if index == 0:
		link.rest = Link(link.first, link.rest)
		link.first = item
	else:
		insert_mut(link.rest, item, index - 1)

