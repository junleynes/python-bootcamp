# TODO: Ask the user for an input that should be a number
number = input("Enter number: ")

# TODO: Then try to convert this into an integer using the following:
try:
    number_converted = int(number)
    print("You entered a valid number")
# The user could provide an invalid integer input (string)
# TODO: Handle this case
except ValueError:
    print ("Enter a valid number")
# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry
