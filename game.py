import random

username = input("Enter your name:")
print("Hello, " + username)
scores = open('rating.txt')
userscore = 0
for row in scores:
    if username == row.split(" ")[0]:
        userscore = int(row.split(" ")[1])
        break
scores.close()

while True:
    input_string = input()
    computer_select = random.choice(["rock", "paper", "scissors"])
    if input_string == "rock" and computer_select == "paper" or \
            input_string == "paper" and computer_select == "scissors" or \
            input_string == "scissors" and computer_select == "rock":
        print("Sorry, but the computer chose " + computer_select)
    elif input_string == computer_select:
        print("There is a draw (" + computer_select + ")")
        userscore += 50
    elif input_string == "!exit":
        print("Bye!")
        break
    elif input_string == "!rating":
        print("Your rating: " + str(userscore))
    elif input_string in ["rock", "paper", "scissors"]:
        print("Well done. The computer chose " + computer_select + " and failed")
        userscore += 100
    else:
        print("Invalid input")
