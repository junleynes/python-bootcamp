# TODO: Ask the user how many items will be calculated
total = 0
input_count = int(input("How many items will be calculated? "))

# TODO: Use a for loop to ask for more than one cost and count

for x in range(input_count):
    item_cost = int(input("How much is the new item? "))
    item_count = int(input("How many is the new item? "))
    item_total = item_cost * item_count
    total += item_total
    print(item_total)
    print()
print()
print(f"The total is {total}")

