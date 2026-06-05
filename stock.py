stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_value = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stocks:
        investment = stocks[stock_name] * quantity
        total_value += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_value)

file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_value))
file.close()

print("Result saved in portfolio.txt")