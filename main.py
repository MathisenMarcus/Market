from classes import *

myList = Markets(2000) 

#s = input("Give me number:")
#print(s) 

def createMarket(market_list, name_of_market, totalNumber):
	aMarket = Market()
	aMarket.changeNumberOfShoes(totalNumber)
	aMarket.changeName(name_of_market)
	market_list.addMarkets(aMarket)

def closeMarket(market_list, number_sold):
	market_list.updateInventory(number_sold)


createMarket(myList, "Norrkoping", 200)
createMarket(myList, "Kumla", 1000)
#myList.getList()[0].displayName()

print myList.inventory

closeMarket(myList, 55)

print myList.inventory

closeMarket(myList, 2000)

print myList.inventory

for market in myList.getList():
	market.displayName()
	market.displayTotal()
	market.displaySold()

	