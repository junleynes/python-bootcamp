from random import choice
# TODO: Ask the user for an input
user_choice = input("Pick a choice (rock/paper/scissors): ")

# TODO: Make a random choice for the computer
# Note: Read the slide for this part
options = ["rock", "paper", "scissors"]
cpu_choice = choice(options)
print(cpu_choice)

# TODO: Determine if the user wins, the cpu wins, or its a draw

# Challenge: TODO: Robust Input
# Challenge: TODO: Multi-rounds
if user_choice == "rock" and  cpu_choice == "scissor":
    print("You Win!")
elif user_choice == "rock" and  cpu_choice == "paper":
    print("You Lost!")
elif user_choice == "rock" and  cpu_choice == "rock":
    print("Draw!")
elif user_choice == "paper" and  cpu_choice == "scissor":
    print("You Lost!")
elif user_choice == "paper" and  cpu_choice == "paper":
    print("Draw!")
elif user_choice == "paper" and  cpu_choice == "rock":
    print("You Win!")
elif user_choice == "scissor" and  cpu_choice == "scissor":
    print("Draw!")
elif user_choice == "scissor" and  cpu_choice == "paper":
    print("You Win!")
elif user_choice == "scissor" and  cpu_choice == "rock":
    print("You Lost!")

