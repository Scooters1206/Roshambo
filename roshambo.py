import random

print("Let's play Ro-Sham-Bo!")

options = ["Ro", "Sham", "Bo"]

computer_choice = random.choice(options)

user_choice = input("Make your choice: Ro, Sham, Bo?")

if user_choice == "Ro":
    if computer_choice == "Sham":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you win")
    elif computer_choice == "Bo":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you lose")
    elif computer_choice == "Ro":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you tie")
elif user_choice == "Sham":
    if computer_choice == "Bo":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you win")
    elif computer_choice == "Ro":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you lose")
    elif computer_choice == "Sham":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you tie")
elif user_choice == "Bo":
    if computer_choice == "Ro":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you win")
    elif computer_choice == "Sham":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you lose")
    elif computer_choice == "Bo":
        print(f"You chose {user_choice}, and the computer chose {computer_choice}, you tie")   
else :
    print("I don't understand that choice, please write your answer (case sensitive!).")

