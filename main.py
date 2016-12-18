from classes import *


myList = Markets(2000) 

#s = raw_input("Give me number:")
#print s 

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

myList.displayInformation(myList)

programState = True
while programState:
	print "Valkommen till Uncle Marknadsprogram"
	myInput = raw_input("Avsluta? (Ja / Nej): ")
	if myInput == 'Ja':
		print "Du avslutar nu programmet!"
		programState = False
	elif myInput == 'Nej':
		print "Du fortsatter med programmet!"