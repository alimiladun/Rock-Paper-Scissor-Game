import random

user_wins = 0
computer_wins = 0
draw = 0

options = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        print("put valid word")
        continue
    random_number = random.randint(0,2)
    # rick: 0 , paper: 1 scisser: 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("you win")
        user_wins += 1
    

    elif user_input == "paper" and computer_pick == "rock":
        print("you win")
        user_wins += 1
    

    elif user_input == "scissor" and computer_pick == "paper":
        print("you win")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("Draw")
        draw +=1
    
    else:
        print("YOu lost")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Draw", draw,"times.")
print("Good bye See you soon!")

