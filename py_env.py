import math
import operator as op

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
        "+"   : op.add,
        "-"   : op.sub,
        "*"   : op.mul,
        "/"   : op.truediv,
        ">"   : op.gt,
        "<"   : op.lt,
        "="   : op.eq,
        ">="  : op.ge,
        "<="  : op.le,
        "car" : lambda x: x[0],
        "cdr" : lambda x: x[1:],
        "cons": lambda x,y: [x] + y,
    })
    return env

global_env = standard_env()
