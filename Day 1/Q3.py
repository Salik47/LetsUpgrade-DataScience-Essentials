cost_price = int(input("Input1: "))
selling_price = int(input("Input2: "))

if cost_price < selling_price:
    print("Profit")
elif cost_price > selling_price:
    print("Loss")
else:
    print("Neither")
