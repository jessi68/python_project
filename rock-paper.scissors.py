# Write your code here
import secrets


def getScore(user, rating_file):
    
    lines = rating_file
    
    for line in lines:
        line = line.rstrip().split()
        name = line[0]
        score = int(line[1])
        
        if name == user:
            return score
    return 0
    


rock_choice = ["scissors","rock", "paper"]
scissors_choice = ["paper", "scissors","rock"]
paper_choice = ["rock", "paper", "scissors"]

name = input("Enter your name: ")    
print(f"Hello, {name}")

rating_file = open('rating.txt', 'r')

wins = {"rock" : "scissors", "scissors" : "paper", "paper" : "rock"}
options  = ["rock", "fire", "scissors", "snake", "human", "tree",
"wolf", "sponge", "paper", "air", "water", "dragon", "devil", "lightning",
"gun"]

score = getScore(name, rating_file)

computer_options = input()


if computer_options == '':
    computer_options = ["rock", "scissors", "paper"]    
else:
    computer_options = computer_options.split(",")
print("Okay, let's start")

while True:
    
    user_choice = input()
    
    if user_choice == "!rating":
        
        print(f"Your rating: {score}")
        
        continue
    elif user_choice == "!exit":
        break
    elif user_choice not in computer_options:
        print("Invalid input")
        
        continue    

    user_choice = options.index(user_choice)
    numOfOption = len(options)
    computer_choice = secrets.choice(computer_options)
    computer_choice = options.index(computer_choice)

    
   
    user_wins = [(user_choice + index) % numOfOption for index in range(1, 8)]
    
    
    if computer_choice in user_wins:
        score += 100
        
        print(f"Well done. The computer chose {options[computer_choice]} and failed")     
    elif user_choice == computer_choice:
        score += 50
        
        print(f"There is a draw ({options[computer_choice]})")
    else:
        print(f"Sorry, but the computer chose {options[computer_choice]}")
        
  
        
   
        
print("Bye!")
        
rating_file.close()
