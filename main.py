from functions import *

capitals = load_capitals()
capitals_items = capitals.items()

answer_list = game_data(capital_data=capitals)

randomcity = answer_list[0]
correct_capital = answer_list[1]

while True:
    print("What is the capital of {0}?".format(str(list(list(capitals_items)[randomcity])[0])))
    answer = input("Insert answer: ")
    if answer == correct_capital:
        print("You gooooot it! Good job!")
        break
    else:
        print("Wrong answer!")
