def spend(expenses):
    """TODO: Add a new cost in expenses"""
    additional_cost = int(input("What is the additional cost?: "))
    expenses.append(additional_cost)

def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    expenses.pop(-1)

def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(expenses)
    print(sum(expenses))

def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "exit":
            running = False
        else:
            print("Incorrect command.")


main()
