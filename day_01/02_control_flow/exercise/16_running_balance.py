total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        # TODO: Ask for number
        number = int(input("Input a number: "))
        # TODO: Add that number to the total
        total += number
        # TODO: Print the current total
        print (total)
        pass
    if command == "sub":
        # TODO: Ask for number
        number = int(input("Input a number: "))
        # TODO: Sub that number to the total
        total -= number
        # TODO: Print the current total
        print(total)
        pass
    if command == "mul":
        # TODO: Ask for number
        number = int(input("Input a number: "))
        # TODO: Sub that number to the total
        total *= number
        # TODO: Print the current total
        print(total)
        pass
    if command == "div":
        # TODO: Ask for number
        number = int(input("Input a number: "))
        # TODO: Sub that number to the total
        total /= number
        # TODO: Print the current total
        print(total)
        pass
    if command == "clear":
        # TODO: Sub that number to the total
        total = 0
        # TODO: Print the current total
        print(total)
        pass
    elif command == "exit":
        running = False


