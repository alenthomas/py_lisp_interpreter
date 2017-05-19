from py_env import global_env

def tokenize(string):
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

def lisp_ast(tokens):
    if not tokens:
        raise SyntaxError("unexpected EOF while reading")
    token = tokens.pop(0)
    if token is "(":
        _list = list()
        while tokens[0] is not ")":
            _list.append(lisp_ast(tokens))
        tokens.pop(0)
        return _list
    elif token is ")":
        raise SyntaxError("unexpected ')'")
    else:
        return atom(token)

def parse(lisp_string):
    tokens = tokenize(lisp_string)
    if tokens.count("(") != tokens.count(")"):
        raise SyntaxError("unbalanced parenthesis")
    else:
        ast = lisp_ast(tokens)
        print(ast)
        return ast

def lisp_eval(x, env):
    if isinstance(x, str):
        return env[x]
    elif not isinstance(x, list):
        return x
    elif x[0] == "if":
        (_, condition, true_exp, false_exp) = x
        exp = (true_exp if lisp_eval(condition, env) else false_exp)
        return lisp_eval(exp, env)
    elif x[0] == "define":
        (_, var, exp) = x
        env[var] = lisp_eval(exp, env)
    else:
        function = lisp_eval(x[0], env)
        args = [lisp_eval(arg, env) for arg in x[1:]]
        return function(*args)

def interface():
    string = input()
    parsed = parse(string)
    print("AST", parsed)
    result = lisp_eval(parsed, global_env)
    print(result)

if __name__ == "__main__":
    interface()
