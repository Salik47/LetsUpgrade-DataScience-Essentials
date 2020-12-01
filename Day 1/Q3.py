cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if cost_price < selling_price:
    print("Profit")
elif cost_price > selling_price:
    print("Loss")
else:
    print("Neither")
