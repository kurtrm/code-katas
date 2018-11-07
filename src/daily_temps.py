"""
"""


def slow_daily_temps(T):
    """
    """
    days = []
    for i, temp in enumerate(T, start=1):
        for i, next_day in enumerate(T[i:], start=1):
            if next_day > temp:
                days.append(i)
                break
        else:
            days.append(0)
    return days


def fast_daily_temps(T):
    """
    """
    
