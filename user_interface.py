import complex_module as cm
import rational_module as rm
import logger as lg
from fractions import Fraction


def start():
    match input('С какими числами хотите выполнить операцию (c - комплексные, r - рациональные)?: '):
        case 'c':
            exp = input('Введите выражение через пробел: ').split()
            if complex(exp[0]) and complex(exp[-1]) and exp[1] in {'+', '-', '*', '/'}:
                return lg.complex_logger(exp, cm.calculate(exp))

            else:
                print('Введены не верные данные!')


        case 'r':
            exp = input('Введите выражение через пробел: ').split()
            if Fraction(exp[0]) and Fraction(exp[-1]) and exp[1] in {'+', '-', '*', '/'}:
                return lg.rational_logger(exp, rm.calculate(exp))

            else:
                print('Введены не верные данные!')






