even_numbers = []

print("Enter 10 `numbers")
for i in range(0, 10):
    num = int(input("Enter the " + str(i + 1) + " number: "))

    if num % 2 == 0 and num != 0:
        even_numbers.append(num)

print("\nThe even even_numbers are:", even_numbers)
