# TODO: Fill in the details of the item you plan to buy
order_info = {
    "Name": "MacBook Pro",
    "Info": "High-performance laptop line available in 14-inch and 16-inch sizes powered by Apple silicon",
    "Price": "P139,990"
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""
def order_details(order):
    for order_keys, order_values in order.items():
        print(order_keys,":",order_values)

order_details(order_info)