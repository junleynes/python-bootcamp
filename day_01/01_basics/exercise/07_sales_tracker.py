# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("How much is the 1st item? "))  # Let the user enter a number
item_count_1 = int(input("How many pax for the 1st item? "))  # Let the user enter a number

item_cost_2 = int(input("How much is the 2nd item? "))   # Let the user enter a number
item_count_2 = int(input("How many pax for the 2nd item? "))  # Let the user enter a number

item_cost_3 = int(input("How much is the 3rd item? "))   # Let the user enter a number
item_count_3 = int(input("How many pax for the 2nd item? "))  # Let the user enter a number
print ()
# Calculate the total
total = item_cost_1 * item_count_1 + item_cost_2 * item_count_2 + item_cost_3 * item_count_3
print(f"The total price is = {total}")
print(f"The total price of {item_cost_1} x {item_count_1} + {item_cost_2} x {item_count_2} + {item_cost_3} x {item_count_3} is = {total}")