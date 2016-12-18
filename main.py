from classes import *


myList = Markets(2000) 

#s = input("Give me number:")
#print(s) 

def createMarket(market_list, name_of_market, totalNumber):
	aMarket = Market()
	aMarket.setDate()
	aMarket.changeNumberOfShoes(totalNumber)
	aMarket.changeName(name_of_market)
	market_list.addMarkets(aMarket)

def closeMarket(market_list, number_sold):
	market_list.updateInventory(number_sold)


createMarket(myList, "Norrkoping", 200)
createMarket(myList, "Kumla", 1000)
#myList.getList()[0].displayName()

year = datetime.date.today().year


print year

for market in myList.getList():
	market.displayName()
	market.displayTotal()
	market.displaySold()
	market.printDate()

	