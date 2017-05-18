from py_env import global_env

def tokenize(string):
    '''
    program = "(begin (define r 10))"
    tokenize(program)
    ['(', 'begin', '(', 'define', 'r', '10', ')', ')']
    '''
    tokens = string.replace("(", " ( ").replace(")", " ) ").split()
    return tokens

def atom(token):
    '''
    return the value of token
    precedence: int, float, str
    '''
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return str(token)

def lisp_ast(tokens):
    '''
    recursivley reads through tokens
    returns an AST in the form of a list
    '''
    if not tokens:
        raise SyntaxError("unexpected EOF while reading")
    token = tokens.pop(0)
    if token is "(":
        new_list = list()
        while tokens[0] is not ")":
            new_list.append(lisp_ast(tokens))
        tokens.pop(0)
        return new_list
    elif token is ")":
        raise SyntaxError("unexpected ')'")
    else:
        return atom(token)

def parse(lisp_string):
    '''
    program = "(begin (define r 10) (* pi (* r r)))"
    parse(program)
    ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]
    '''
    return lisp_ast(tokenize(lisp_string))

def lisp_eval(x, env):
    '''
    Evaluate an expression in an environment
    '''
    print("first x:", x)
    if isinstance(x, str):
        '''
        checks for string;
        specifically our keywords/operators
        if found returns the corresponding python function
        '''
        print("isinstance str:", x)
        print("env[x]:", env[x])
        return env[x]
    elif not isinstance(x, list):
        '''
        checks if not a list
        else it should be a literal specifically atom
        '''
        print("isinstance list:", x)
        return x
    elif x[0] == "if":
        '''
        if the condition is 'if' evaluate it in python
        call the eval with the output of if expression
        '''
        (_, condition, true_exp, false_exp) = x
        exp = (true_exp if lisp_eval(condition, env) else false_exp)
        return lisp_eval(exp, env)
    elif x[0] == "define":
        (_, var, exp) = x
        env[var] = lisp_eval(exp, env)
    else:
        '''
        if not (list, keyword, number)
        probably expression
        '''
        print("in else, calls eval with first arg:", x[0])
        proc = lisp_eval(x[0], env)
        print("proc :", proc)
        print("x[1:] :", x[1:])
        args = [lisp_eval(arg, env) for arg in x[1:]]
        print("args :", args)
        print("proc(*args) :", proc(*args))
        return proc(*args)

def interface():
    string = input()
    parsed = parse(string)
    print("AST", parsed)
    result = lisp_eval(parsed, global_env)
    print("Result", result)

interface()
