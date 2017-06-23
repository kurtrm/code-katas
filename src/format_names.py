"""Kata: Format a list of hashes in a string

#1 Best Practices Solution marceltschoppch & Others

def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
"""


def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return ' & '.join([dicty['name'] for dicty in names])
    first_few = ', '.join([dicty['name'] for dicty in names[:-2]])
    last_two = ' & '.join([dicty['name'] for dicty in names[-2:]])
    return ', '.join([first_few, last_two])
