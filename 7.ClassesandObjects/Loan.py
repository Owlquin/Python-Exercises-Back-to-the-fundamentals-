"""
(The
Stock class) Design a class named Stock to represent a company's stock
that contains:
■ A private string data field named symbol for the stock's symbol.
■ A private string data field named name for the stock's name.
■ A private float data field named previousClosingPrice that stores the stock
price for the previous day.
■ A private float data field named currentPrice that stores the stock price for
the current time.
■ A constructor that creates a stock with the specified symbol, name, previous
price, and current price.
■ A get method for returning the stock name.
■ A get method for returning the stock symbol.
■ Get and set methods for getting/setting the stock's previous price.
■ Get and set methods for getting/setting the stock's current price.
■ A method named getChangePercent() that returns the percentage changed
from previousClosingPrice to currentPrice.
Draw the UML diagram for the class, and then implement the class. Write a test
program that creates a Stock object with the stock symbol INTC, the name Intel
Corporation, the previous closing price of 20.5, and the new current price of
20.35, and display the price-change percentage
"""

class Stock:    
    def __init__(self, symbol,name,previousClosingPrice,currentPrice):
        self.__symbol = str(symbol)
        self.__name = str(name)
        self.__previousClosingPrice = float(previousClosingPrice)
        self.__currentPrice = float(currentPrice)

    def getStockName(self): #make it accessible for the user with get
        return self.__name

    def getStockSymbol(self):
        return self.__symbol

    def getStockPreviousPrice(self):
        return self.__previousClosingPrice 

    def setStockPreviousPrice(self,previousClosingPrice): # to enable data field to be modified with set
         self.__previousClosingPrice = float(previousClosingPrice)

    def getStockCurrentPrice(self):
        return self.__currentPrice

    def setStockCurrentPrice(self,currentPrice):
         self.__currentPrice = float(currentPrice)

    def getChangePercent(self):
        return (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice * 100

    
