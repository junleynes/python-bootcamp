# TODO: Ask the user for an input that should be a number

# TODO: Then try to convert this into an integer using the following:
def askinput():
    while True:
        try:
            number = input("Enter number: ")
            number_converted = int(number)
            print(number)
            if number_converted < 0:
                raise ValueError()
        # The user could provide an invalid integer input (string)
        # TODO: Handle this case
        except ValueError:
            print ("Enter a valid number")
        # The user could give a negative number
        # TODO: Handle this case

        # Challenge: TODO: Give the user infinite times to retry

askinput()
