from functools import reduce

def add(*args):
    if args:
        return reduce((lambda x,y: x+y), args)
    else:
        return 0

def sub(*args):
    if len(args) == 1:
        return -args[0]
    else:
        return reduce((lambda x,y: x-y), args)

def mul(*args):
    if args:
        return reduce((lambda x,y: x*y), args)
    else:
        return 1

def div(*args):
    if len(args) == 1:
        return 1/args[0]
    else:
        return reduce((lambda x,y: x/y), args)
