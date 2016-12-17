class Markets:

	def __init__(self,myInventory):
		self.marketList = []
		self.inventory = myInventory

	def addMarkets(self,market):
		self.marketList.append(market)
	def sizeOfMarkets(self):
		len(self.marketList)

	def getList(self):
		return self.marketList
	def updateInventory(self,sold):
		if (self.inventory - sold) >= 0:
			self.inventory = self.inventory - sold
		else:
			print "Inventory empty"
			


class Market:

	def __init__(self):
		self.totalNumberOfShoes = 0
		self.numberSold = 0
		self.marketName = "NoName"

	def changeNumberOfShoes(self,total):
		self.totalNumberOfShoes = total
	def changeNumberOfSold(self,sold):
		self.numberSold = sold
	def changeName(self,name):
		self.marketName = name

	def displayTotal(self):
		print "Total number of shoes: " + str(self.totalNumberOfShoes)
	def displaySold(self):
		print "Number of shoes sold: " + str(self.numberSold)
	def displayName(self):
		print "Name of market: " + self.marketName 




