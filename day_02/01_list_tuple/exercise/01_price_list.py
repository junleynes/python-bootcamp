prices = [10_000, 20, 3_000, 3, -200, 1_000]

# TODO: Print the first, third, and last item
print(f"Current Price: {prices[0]}")
print(f"Current Price: {prices[2]}")
print(f"Current Price: {prices[-1]}")
print()
indeces = [0,2,-1]
for n in indeces:
    print("Current Price:", prices[n])