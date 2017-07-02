"""Script for extracting values from Forbes top 40 billionaries."""
import json


def main():
    """Find the oldest under 80 and youngest billionaires."""
    with open('src/forbes.json') as json_forbes:
        python_forbes = json.load(json_forbes)

    max_age = 80
    highest_age = 0
    smallest_age = 0
    youngest = ''
    oldest = ''
    for billionaire in python_forbes:
        if billionaire['age'] < 0:
            continue
        if billionaire['age'] < max_age and billionaire['age'] > highest_age:
            highest_age = billionaire['age']
            oldest = billionaire
        elif billionaire['age'] < smallest_age or smallest_age == 0:
            smallest_age = billionaire['age']
            youngest = billionaire

    return [oldest['name'],
            str(oldest['net_worth (USD)']),
            oldest['source'],
            youngest['name'],
            str(youngest['net_worth (USD)']),
            youngest['source']]


if __name__ == '__main__':  # pragma no cover
    returns = main()
    print('The oldest billionaire under 80 is {}. '
          'Her/His net worth is ${} billion and made their billions at {}.'
          .format(
              returns[0],
              str(returns[1]),
              returns[2])
          )

    print('The youngest billionaire is {}. '
          'Their net worth is ${} billion and made their billions at {}.'
          .format(
              returns[3],
              str(returns[4]),
              returns[5])
          )
