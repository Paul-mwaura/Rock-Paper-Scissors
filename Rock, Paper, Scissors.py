#Author Paul Mwaura

import random

def game1():
    while True:
        list1 = ["rock", "paper", "scissors"]
        option = input("Select option: ")
        t = random.choice(list1)
        if option == list1[0]:
            print(t)
            print("\n")
            if t == "paper":
                print("You lost")
            elif t == "scissors":
                print("You won")
            else:
                print("It's a tie")
        elif option == list1[1]:
            print(t)
            if t == "scissors":
                print("You lost")
            elif t == "rock":
                print("You won")
            else:
                print("It's a tie")
        elif option == list1[2]:
            print(t)
            if t == "rock":
                print("You lost")
            elif t == "paper":
                print("You won")
            else:
                print("It's a tie")
        else:
            print("invalid option!!!")
        print("\n")
game1()



