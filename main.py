# rock paper scissors game
import random


def choice():
    user = input("enter your choice, 'r' for rock , 'p' for paper , 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])
    print(f"choice of the computer was '{computer}'")
    if user == computer:
        return "it's a tie "
    if won(user, computer):
        return f"Yay , you won with '{user}' "
    return f"You lost with '{user}'"


def won(user, computer):
    if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        return True


print(choice())
