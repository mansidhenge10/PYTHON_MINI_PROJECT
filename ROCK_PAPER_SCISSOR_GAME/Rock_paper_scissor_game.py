### workflow ###
""" 
i-input from user(rock, paper, scissor)
2-computer choice(rock, paper, scissor randomly not conditionally)
3- result print
cases:-
A-rock
rock-rock=tie
rock-paper- paper win
rock-scissor- rock win

B- paper
paper-paper= tie
paper-rock-paper win
paper-scissor-scissor win  

C: scissor 
scissor-scissor= tie
scissor-rock= rock win
scissor- paper= scissor win
"""
import random 
item_list=[ "Rock", "paper", "scissor"]
user_choice=input("enter your choice=")
comp_choice=random.choice(item_list)

print(f"user choice= {user_choice},computer choice ={comp_choice}")

if user_choice == comp_choice:
    print("match is draw")
elif user_choice == "Rock":
    if comp_choice == "paper":
        print("computer win !")
    else:
        print("you win !")
elif user_choice == "paper":
    if comp_choice == "scissor":
        print("computer win !")
    else:
        print("you win !")
elif user_choice == "scissor":
    if comp_choice == "Rock":
        print("computer win !")
    else:
        print("you win !")
else:
    print("invalid choice")
        
        

