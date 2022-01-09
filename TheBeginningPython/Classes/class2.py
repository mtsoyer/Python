class Pizza:
	def __init__(self, name, size, flavour):
		self.name = name
		self.size = size
		self.flavour = flavour
		self.number = 0000
		
	def receipt(self):
		print(f"{self.name} ordered a {self.size} {self.flavour} pizza. ID: {self.number}")
	def updateno(self, no):
	  		if (self.number >= no):
	  			print("You cant reduce IDs")
	  		else:
	  			self.number = no
  
	def inco(self, add):
	 self.number += add

class resdetail:
	def __init__(self, loc = 'South africa'):
		self.loc = loc
		self.man = "Jack"
	def detail(self):
		print(f"The resturant's location is {self.loc}")
	def manager(self):
		print(f"the manager's name is {self.man}")

class resturant(Pizza, resdetail):
	def __init__(self, name, size, flavour, ):
		super().__init__(name, size, flavour)
		self.resturant = ""
		self.resloc =resdetail()
	def place(self, place):
		self.resturant = place
		print(f"You ordered from {self.resturant}")
	def receipt(self):
		print(f"{self.name} ordered a {self.size} {self.flavour} pizza. ID: {self.number} from {self.resturant}")


