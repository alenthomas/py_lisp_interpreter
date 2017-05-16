def tokenize(string):
    '''
    program = "(begin (define r 10))"
    tokenize(program)
    ['(', 'begin', '(', 'define', 'r', '10', ')', ')']
    '''
    return string.replace('(', ' ( ').replace(')', ' ) ').split()
def parse():
    '''
    program = "(begin (define r 10) (* pi (* r r)))"
    parse(program)
    ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]
    '''
    pass

def eval():
    '''
    eval(parse(program))
    314.1592653589793
    '''
    pass

def interface():
    string = input()
    tokens=tokenize(string)
    print(tokens)



interface()
