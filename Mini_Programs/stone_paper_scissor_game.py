a=["stone","paper","scissor"]
import random
system_choice=random.choice(a)
user_choice=input("Enter your choice (stone, paper, scissor): ").lower()
print("System choice:", system_choice)
if user_choice==system_choice:
    print("It's a tie!")
elif (user_choice=="stone" and system_choice=="scissor") or (user_choice=="paper" and system_choice=="stone") or (user_choice=="scissor" and system_choice=="paper"):    
    print("You win!")
elif (user_choice=="stone" and system_choice=="paper") or (user_choice=="paper" and system_choice=="scissor") or (user_choice=="scissor" and system_choice=="stone"):    
    print("System wins!")
else:
    print("Invalid input! Please enter stone, paper, or scissor.")    
