from functions import *

capitals = load_capitals()

randomcity = game_data(capital_data=capitals)[0]
correct_capital = game_data(capital_data=capitals)[1]

while True:
    print("What is the capital of {0}?".format(str(list(list(capitals.items())[randomcity])[0])))
    answer = input("Insert answer: ")
    if answer == correct_capital:
        print("You gooooot it! Good job!")
        break
    else:
        print("Wrong answer!")
