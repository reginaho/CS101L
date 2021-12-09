import math
def total(values):
    sum = 0
    for i in values:
        sum += i
    return sum
def average(values):
    if len(values) == 0:
        return math.nan
    average_value = (total(values) / len(values))
    return average_value
def median(values):
    if len(values) == 0:
        raise ValueError
    elif len(values) % 2 == 1:
        return sorted(values)[len(values)//2]
    else:
        return average([sorted(values)[len(values)//2], sorted(values)[(len(values)//2) - 1]])