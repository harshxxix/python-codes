import random

user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

computer_choice = random.randint(0,2)

print(computer_choice)

if(user_choice == computer_choice):
    print("Tie!")

elif (user_choice == 0 and computer_choice == 2 or
user_choice == 1 and computer_choice == 0 or
user_choice == 2 and computer_choice == 1):
    print("You win!")
       

else:
    print("Computer win!")     