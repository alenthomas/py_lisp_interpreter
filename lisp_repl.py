from py_lisp import lisp_eval, parse

def repl(prompt="=>"):
    while True:
        val = lisp_eval(parse(input(prompt)))
        if val is not None:
            print(val)

if __name__ == "__main__":
    repl()
