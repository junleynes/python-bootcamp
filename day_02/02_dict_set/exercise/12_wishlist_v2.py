# TODO: Fill in the details of the items you plan to buy
orders = [
    {
    "Name": "Macbook Pro",
    "Info": "High-performance laptop line available in 14-inch and 16-inch sizes powered by Apple silicon"
    },
    {
    "Name": "Mac Pro",
    "Info": "High-performance desktop powered by Apple silicon"
    }
]

# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
for order in orders:
    print("Order:")
    for key, value in order.items():
        print(f"\t {key}: {value}")