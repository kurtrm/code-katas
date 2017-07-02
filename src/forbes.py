"""Script for extracting values from Forbes top 40 billionaries."""
import json


with open('forbes.json') as json_forbes:
    python_forbes = json.load(json_forbes)

max_age = 80
highest_age = 80
oldest = 0
youngest = 0
for index, billionaire in enumerate(python_forbes):
    if billionaire['age'] < 80 and billionaire['age'] > highest_age:
        oldest = index
    if billionaire['age'] < youngest or youngest == 0:
        youngest = index

