newAmount = 0
while True:
    amountDollars = input("How many US Dollars do you want to exchange?")
    if amountDollars.isdigit() == False:
        break
    #else:
    currencyName = input("\nEnter the name of the currency you are converting dollars to: ")
    exchangeRate = input("\nWhat is the exchange rate?")
    if exchangeRate.isdigit() == False:
        break
    break

newAmount = int(amountDollars) * int(exchangeRate)
print()
print(newAmount)

