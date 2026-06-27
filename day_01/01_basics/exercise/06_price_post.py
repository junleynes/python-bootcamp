# Price notification template
price_notification = "The price of {} is ${}."

# TODO: Post: Latte ($3.5)
coffee = "Latte"
price = 3.5
formatted_price_notification = price_notification.format(coffee, price)
print(formatted_price_notification)

# TODO: Post: Espresso ($2.75)
coffee = "Espresso"
price = 2.75
formatted_price_notification = price_notification.format(coffee, price)
print(formatted_price_notification)

# TODO: Post: Cappuccino ($4.0)
coffee = "Espresso"
price = 4.0
formatted_price_notification = price_notification.format(coffee, price)
print(formatted_price_notification)
print()
# TODO: Post: Latte ($3.5)
coffee = "Latte"
price = 3.5
print(price_notification.format(coffee, price))

# TODO: Post: Espresso ($2.75)
coffee = "Espresso"
price = 2.75
print(price_notification.format(coffee, price))

# TODO: Post: Cappuccino ($4.0)
coffee = "Espresso"
price = 4.0
print(price_notification.format(coffee, price))