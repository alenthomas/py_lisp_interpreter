def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def sub(*args):
    total = 0
    for num in args:
        total -= num
    return total

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return total

def div(*args):
    total = 1
    for num in args:
        total /= num
    return total
