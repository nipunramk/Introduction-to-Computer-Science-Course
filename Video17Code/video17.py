class Car:
	num_wheels = 4
	def __init__(self, model, color):
		self.model = model
		self.color = color
		self.gas = 20	

	def __repr__(self):
		return 'Car(' + self.model +', ' + self.color + ')'

	def __str__(self):
		return self.color + ' ' + self.model

	def drive(self, used_gas):
		if used_gas > self.gas:
			return 'I need more gas!'
		else:
			print('Vroom!')
			self.gas = self.gas - used_gas

	def fill_gas(self):
		self.gas = 20
		print("I have a full tank!")		

class Account:
	"""Represent a general version of how
	an account works"""
	interest = 0.02
	def __init__(self, name):
		self.name = name
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount
		return self.summary()

	def summary(self):
		return 'Your balance is {0} dollars'.format(self.balance) 

	def withdraw(self, amount):
		if self.balance < amount:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.summary() 

class CheckingAccount(Account):
	"""A withdrawal fee is included in the CheckingAccount
	"""
	withdrawal_fee = 1
	def withdraw(self, amount):
		"""Slight difference of because of fee"""
		return Account.withdraw(self, amount + self.withdrawal_fee)

class SavingsAccount(Account):
	"""A deposit fee is included"""
	deposit_fee = 2
	def deposit(self, amount):
		return Account.deposit(self, amount - self.deposit_fee)



	



