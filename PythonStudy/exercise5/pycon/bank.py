class Account:
	def __init__(self, name, number, balance):
	   self.name = name
	   self.number = number
	   self.balance = balance

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError('amount must be positive')
		self.balance = self.balance + amount

	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimeError('account is not enoght')
		self.balance = self.balance - amount

	#預設不能用 __str__
	#會顯示物件的記憶體位址
	def __repr__(self):
		return 'Account({0}, {1}, {2})'.format(self.name, self.number, self.balance)
		