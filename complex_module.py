
def calculate(exp):
    a, b, c = exp
    match b:
        case '+':
            return complex(a) + complex(c)
        case '-':
            return complex(a) - complex(c)
        case '*':
            return complex(a) * complex(c)
        case '/':
            return complex(a) / complex(c)


