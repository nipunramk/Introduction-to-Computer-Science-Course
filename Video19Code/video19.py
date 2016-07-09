def create_board(n, m):
	"""Creates a two dimensional 
	n (rows) x m (columns) board filled with zeros
	4 x 5 board
	0 0 0 0 0 
	0 0 0 0 0
	0 0 0 0 0 
	0 0 0 0 0
	3 x 2 board 
	0 0
	0 0 
	0 0	
	>>> create_board(4, 5)
	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	>>> create_board(3, 2)
	[[0, 0], [0, 0], [0, 0]]
	"""
	if n == 0 or m == 0:
		raise IndexError("dimensions cannot both be zero")
	if n < 0 or m < 0:
		raise IndexError("dimensions cannot be negative")
	board = []
	rows = [0] * m
	for i in range(n):
		board.append(rows)
	return board
	
def invert(x):
	"""A special invert function that will
	return 1/x, except in the case that we pass in
	x = 0, in which case we return 1
	"""
	try:
		return 1 / x
	except ZeroDivisionError as e:
		print(e)
		return 1

class RangeIterable:
	"""Implements the __iter__ method,
	making objects of the class iterable"""
	def __init__(self, start, end):
		self.start = start
		self.end = end
	def __iter__(self):
		return RangeIterator(self.start, self.end)

class RangeIterator:
	"""Implements both __iter__ and
	__next__ methods, making objects of this
	class function as both iterables and iterators
	"""
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.current = start

	def __next__(self):
		if self.current == self.end:
			self.current = self.start
			raise StopIteration
		result = self.current
		self.current = self.current + 1
		return result
	def __iter__(self):
		return self





