# class Dog:
#	def __init__(self, name, age):
#		self.name = name
#		self.age = age
#	def sit(self):
#		print(f"{self.name} is sitting")
#	def roll(self):
#		print(f"{self.name} is rolling over")
#
#doggie = Dog("Herman", 7)
# doggie.sit()
# doggie.roll()

# class Pizza:
# 	def __init__(self, name, size, flavour):
# 		self.name = name
# 		self.size = size
# 		self.flavour = flavour
# 		self.number = 0000

# 	def receipt(self):
# 		print(f"{self.name} ordered a {self.size} {self.flavour} pizza. ID: {self.number}")
# 	def updateno(self, no):
# 	  		if (self.number >= no):
# 	  			print("You cant reduce IDs")
# 	  		else:
# 	  			self.number = no

# 	def inco(self, add):
# 	 self.number += add


# class resdetail:
# 	def __init__(self, loc = 'South africa'):
# 		self.loc = loc
# 		self.man = "Jack"
# 	def detail(self):
# 		print(f"The resturant's location is {self.loc}")
# 	def manager(self):
# 		print(f"the manager's name is {self.man}")

# class resturant(Pizza, resdetail):
# 	def __init__(self, name, size, flavour, ):
# 		super().__init__(name, size, flavour)
# 		self.resturant = ""
# 		self.resloc =resdetail()
# 	def place(self, place):
# 		self.resturant = place
# 		print(f"You ordered from {self.resturant}")
# 	def receipt(self):
# 		print(f"{self.name} ordered a {self.size} {self.flavour} pizza. ID: {self.number} from {self.resturant}")


from class2 import Pizza, resdetail, resturant


piz = Pizza("Jack", "Large", "Garlic")
piz.inco(78)
piz.receipt()

res = resturant("Jack", "Large", "Garlic")
res.receipt()
res.place("Roman's Pizza")
res.receipt()
res.resloc.detail()
res.resloc.manager()



