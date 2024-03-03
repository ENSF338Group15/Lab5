import sys
if len(sys.argv) > 1:
    exp = sys.argv[1]
else:
    print('Running test expression, if you wish to run with your own expression, run with a commandline argument')
    exp = '(- (* 1 3) (/ 6 (+ 1 2)))'
    exp = '(* (+ 1 5) 2)'
    exp = '(+ 1 5)'


operator_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}


def op(exp: str):
    if '(' not in exp:
        return int(exp)
    else:
        exp = exp.removeprefix('(')
        exp = exp.removesuffix(')')
        o = exp[0]
        exp = exp[2:]
        if exp[0] == '(':
            count = 1
            for index, i in enumerate(exp[1:]):
                # print(f'reach {index}', exp)
                if i == '(':
                    # print(exp[1:index+1])
                    count += 1
                elif i == ')':
                    count -= 1
                if count == 0:
                    break
            n1 = op(exp[:index+2])
            n2 = op(exp[index+3:])
        else:
            index = exp[1:].index(' ')+1
            # print(exp, index, exp[:index], exp[index+1:], sep=';')
            n1 = op(exp[:index])
            n2 = op(exp[index+1:])
        return round(operator_dict[o](n1, n2))


print(op(exp))
