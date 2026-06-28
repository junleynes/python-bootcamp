orders = {}

order = input("Enter order: ")
while order:
    count = int(input("Enter how many: "))


    # TODO: Record the person’s order
    # TODO: If the order already exist, just add the count
    if order in orders:
        orders[order] = orders[order] + count
        print(orders)
    else:
        orders[order] = count
        print(orders)
    order = input("Enter order: ")
print(orders)
