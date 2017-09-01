usd = float(input("What is the amount of US Dollars you wish to convert?"))
exchangeRate = float(input("What is the current exchange rate (1 $US Dollar equals what in the Foriegn Currency"))
foreignCurr = usd * exchangeRate
print("The amount in Foreign Currency is $%1.2f"%(foreignCurr))
