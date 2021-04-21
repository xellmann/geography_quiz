import json
import random

def load_capitals():
    with open("data.json", "r") as file_handle:
        capitals = json.loads(file_handle.read())
    return capitals


def game_data(capital_data):
    randomcity = random.randint(0, len(capital_data.keys())-1)
    correct_capital = str(list(list(capital_data.items())[randomcity])[1])
    return randomcity, correct_capital
