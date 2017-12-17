import requests
import json

with open('exercises.json', 'r') as file:
    d = (json.load(file))
# print(d['exercises']['legs'])

def get_exer(text):
    if text == None:
        return 'Enter the command "press", "legs" or "arms" to get a set of exercises'
    elif text == 'press':
        return d['exercises']['press']
    elif text == 'legs':
        return d['exercises']['legs']
    elif text == 'arms':
        return d['exercises']['arms']
    else:
        return 'Enter the command "press", "legs" or "arms" to get a set of exercises'

# test = get_exer('arms')
# print(test)