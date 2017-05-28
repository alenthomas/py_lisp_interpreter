import math
import operator as op
from helpers import add, sub, mul, div

class Env(dict):

    def __init__(self, params=(), args=(), outer=None):
        self.update(zip(params, args))
        self.outer = outer

    def find(self, var):
        if var in self:
            return self
        else:
            return self.outer.find(var)

def standard_env():
    env = Env()
    env.update({
        "+"   : add,
        "-"   : sub,
        "*"   : mul,
        "/"   : div,
        ">"   : op.gt,
        "<"   : op.lt,
        "="   : op.eq,
        ">="  : op.ge,
        "<="  : op.le,
        "car" : lambda x: x[0],
        "cdr" : lambda x: x[1:],
        "cons": lambda x,y: [x] + y,
        "reverse": lambda x: x[::-1],
    })
    return env

global_env = standard_env()
