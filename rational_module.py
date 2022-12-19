from fractions import Fraction

def calculate(exp):
    a, b, c = exp
    match b:
        case '+':
            return Fraction(a) + Fraction(c)
        case '-':
            return Fraction(a) - Fraction(c)
        case '*':
            return Fraction(a) * Fraction(c)
        case '/':
            return Fraction(a) / Fraction(c)




