import random 
name =input("Enter ur name plz: ")
game = ["P","R","S"]

print("R ----> Rock (or) P ---->  paper (or) S ---> scissors")
#rule = "R" , "S" , "P"

user_inp =input("Chose one of thim (R,P,S) ---> ").upper()


computer_inp =random.choice(game)


if user_inp not in  game:
    print("ERROR")

elif user_inp == computer_inp:
    print("draw")


elif user_inp == 'R' and computer_inp == 'S':
    print(f"{name} won (:")
    
elif user_inp == 'P' and computer_inp == 'R':
    print(f"{name} won (: ")

elif user_inp == 'S' and computer_inp == 'P':
    print(f"{name} won (: ")

else:
    print("computr won ): ")
