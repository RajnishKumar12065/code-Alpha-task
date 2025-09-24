# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 310,
    "GOOGL": 140,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠ Invalid stock symbol. Try again.")
        continue
    
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue
    
    portfolio[stock] = portfolio.get(stock, 0) + qty
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"✅ Added {qty} shares of {stock} (Value: ${investment})")

print("\n----- Your Portfolio -----")
for stock, qty in portfolio.items():
    print(f"{stock} ({qty} shares) -> ${stock_prices[stock] * qty}")

print("--------------------------")
print("💰 Total Investment Value: $", total_investment)

# Save to file
save = input("\nDo you want to save portfolio to file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (portfolio.txt or portfolio.csv): ")
    if filename.endswith(".csv"):
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Value\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock},{qty},{stock_prices[stock] * qty}\n")
            f.write(f"TOTAL,,{total_investment}\n")
    else:  # default .txt
        with open(filename, "w") as f:
            f.write("----- Your Portfolio -----\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock} ({qty} shares) -> ${stock_prices[stock] * qty}\n")
            f.write("--------------------------\n")
            f.write(f"Total Investment Value: ${total_investment}\n")
    print(f"📂 Portfolio saved in {filename}")