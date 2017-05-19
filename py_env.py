import math
import operator as op

Env = dict()

def standard_env():
    env = Env
    env.update({
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        '>': op.gt,
        '<': op.lt,
        '=': op.eq,
        'cons': lambda x: x[0],
        'cdr': lambda x: x[1:],
    })
    return env

global_env = standard_env()
