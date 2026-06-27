items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

for item in items:
    # TODO: If item equals the item_to_find
    #  # print and exit loop
    request_input = input("What item to find? ")
    if request_input == item_to_find:
        print(request_input)
        break
    pass
