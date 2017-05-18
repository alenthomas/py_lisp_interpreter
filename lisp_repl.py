from py_lisp import lisp_eval, parse
from py_env import global_env

def repl(prompt="=>"):
    while True:
        val = lisp_eval(parse(input(prompt)), global_env)
        if val is not None:
            print(val)
