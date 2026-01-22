import random
colours=['Blue','Green','Rose','Red']
print("Guess a colour from the list:",colours)
clr=random.choice(colours)
for i in range(4):
    user=input("Enter a colour:")
    if user not in colours:
        print("Please enter a colour from the list",colours)
    if user==clr:
        print("Your guess is right")
        play_again=input("Do you want to play again[Yes or No]:")
        if play_again=='Yes':
            clr=random.choice(colours)
        elif play_again=='No':
            break
    else:
        print("Try Again")
    clr=random.choice(colours)
            
