#  Creating a origin position
pos = {"x": 0, "y": 0}

n = int(input())

# for loop
for i in range(n):
    move = input().split(" ")      # Accept movement command and store it as alist

    if move[0].lower() == "up":    # Extract direction and compare

        # Increment or decrement appropriate co-ordinates
        pos["y"] += int(move[1])

    elif move[0].lower() == "down":
        pos["y"] -= int(move[1])

    elif move[0].lower() == "left":
        pos["x"] -= int(move[1])

    elif move[0].lower() == "right":
        pos["x"] += int(move[1])


print(int(round((pos["x"]**2 + pos["y"]**2)**0.5)))   # Distance from the orign
