stocks={
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 200
}
print("===== STOK PORTFOLIO TRACKER =====")
name=input("Enter stock name(AAPL/TSLA/GOOG/AMZN): ").upper()
quantity=int(input("Enter quentity: "))
if name in stocks:
    price=stocks[name]
    total=price*quantity
    
    print("Stock:", name)
    print("Price:", price)
    print("Quentity:", quantity)
    print("Total Investment:", total)
else:
    print("Stock not found.")