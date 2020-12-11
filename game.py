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

options_set = input("")
options_set = options_set.split(",")

if len(options_set) <= 1:
    options_set = ['rock', 'paper', 'scissors']
if len(options_set) != len(set(options_set)):
    raise NameError('there is duplicates in list')
if (len(options_set) % 2) != 1:
    raise NameError('Number of items in list must be odd')
print("Okay, let's start")


def run(player_input: str, items_list=None, difficulty='ok') -> int:
    """Prints result of game, returns amount of score to add"""
    if items_list is None:
        items_list = ['rock', 'paper', 'scissors']
    computer_select = random.choice(items_list)
    how_much_items_to_move = items_list.index(player_input) - len(items_list) // 2  # -:from end +: from beginning
    items_perfectized = items_list[how_much_items_to_move:] + items_list[:how_much_items_to_move]
    # print(items_perfectized)
    # print(items_perfectized[:items_perfectized.index(player_input)])  # you won
    if difficulty == 'cheat':
        computer_select = random.choice(items_perfectized[(len(items_perfectized) // 2 + 1):])
    elif difficulty == 'loose':
        computer_select = random.choice(items_perfectized[:len(items_perfectized) // 2])
    elif difficulty == 'draw':
        computer_select = player_input

    if computer_select == player_input:
        print("There is a draw (" + player_input + ")")
        return 50
    elif computer_select in items_perfectized[:len(items_perfectized) // 2]:
        print("Well done. The computer chose " + computer_select + " and failed")
        return 100
    else:
        print("Sorry, but the computer chose " + computer_select)
        return 0


while True:
    input_string = input()
    if input_string == "!exit":
        print("Bye!")
        break
    elif input_string == "!rating":
        print("Your rating: " + str(userscore))
        continue
    elif input_string not in options_set:
        print("Invalid input")
        continue
    else:
        userscore += run(input_string, options_set)
