prices = [10_000, 20, 3_000, 3, -200, 1_000]

# TODO: Print the first, third, and last item
indeces = [0,2,-1]
for n in indeces:
    print("Current Price:", prices[n])
print()
# TODO: Change the first, third, and last values to half the price
for n in indeces:
    prices[n] = (prices[n] // 2)
# TODO: Print the first, third, and last item again to see new price
    print("New Price:", prices[n])
