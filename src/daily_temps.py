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


def stack_daily_temps(T):
    """
    uses two stacks to solve the problem,
    still having complexity issues
    """
    days = []
    stack = []
    reversed_T = T[::-1]
    ref_day = reversed_T.pop()
    next_day = reversed_T.pop()
    num_days = 0
    while len(days) < len(T):
        try:
            num_days += 1
            if next_day > ref_day:
                days.append(num_days)
                reversed_T.append(next_day)
                while stack:
                    reversed_T.append(stack.pop())
                ref_day = reversed_T.pop()
                next_day = reversed_T.pop()
                num_days = 0
            else:
                stack.append(next_day)
                next_day = reversed_T.pop()
        except IndexError:
            days.append(0)
            num_days = 0
            reversed_T.append(next_day)
            while stack:
                reversed_T.append(stack.pop())
            if reversed_T:
                ref_day = reversed_T.pop()
                next_day = reversed_T.pop()
    return days
