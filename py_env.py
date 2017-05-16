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
    })
    return env

global_env = standard_env()