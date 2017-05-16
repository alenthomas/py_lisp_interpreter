def tokenize(string):
    '''
    program = "(begin (define r 10))"
    tokenize(program)
    ['(', 'begin', '(', 'define', 'r', '10', ')', ')']
    '''
    tokens = string.replace("(", " ( ").replace(")", " ) ").split()
    return tokens

def atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return str(token)

def read_from_tokens(tokens):
    if not tokens:
        raise SyntaxError("unexpected EOF while reading")
    token = tokens.pop(0)
    if token is "(":
        new_list = list()
        while tokens[0] is not ")":
            new_list.append(read_from_tokens(tokens))
        tokens.pop(0)
        return new_list
    elif token is ")":
        raise SyntaxError("unexpected ')'")
    else:
        return atom(token)

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
    val = read_from_tokens(tokens)
    print("tokens", tokens)
    print("AST", val)



interface()
