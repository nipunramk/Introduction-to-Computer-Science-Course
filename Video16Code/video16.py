def remove_duplicates(lst):
	"""Returns a list with all duplicate elements
	removed from the list
	>>> remove_duplicates([1, 2, 2, 3, 4, 5, 6, 5, 3, 4, 4, 5, 6, 3, 4, 7, 1, 1, 2])
	[1, 2, 3, 4, 5, 6, 7]
	>>> remove_duplicates([2, 4, 5, 6])
	[2, 4, 5, 6]
	"""
	return list(set(lst))	

def num_common_letters(s1, s2):
	"""Returns the number of common letters between
	string s1 and s2
	>>> num_common_letters('hello', 'worker')
	2
	>>> num_common_letters('intelligence', 'logical') # 'l', 'i', 'g', 'c'
	4
	>>> num_common_letters('yolo', 'death')
	0
	>>> num_common_letters('hello', 'hello')
	4
	>>> num_common_letters('smart', 'tarms')
	5
	"""
	# return len(set([char for char in s1 if char in s2])) one possibility
	return len(set(s1).intersection(set(s2)))


def make_adder(n):
	def adder(k):
		return n + k
	return adder

def make_adder_plus_one(n):
	def adder(k):
		nonlocal n
		n = n + 1
		return n + k
	return adder

def make_balance(deposit):
	"""Mutable function that models a bank account
	"""
	balance = deposit
	def withdraw(amount):
		nonlocal balance
		if amount > balance:
			return 'Insufficient funds!'
		balance = balance - amount
		return balance
	return withdraw

class Car:
	num_wheels = 4
	def __init__(self, model, color):
		self.model = model
		self.color = color
		self.gas = 20

	def drive(self, used_gas):
		if used_gas > self.gas:
			return 'I need more gas!'
		else:
			print('Vroom!')
			self.gas = self.gas - used_gas

	def fill_gas(self):
		self.gas = 20
		print("I have a full tank!")

