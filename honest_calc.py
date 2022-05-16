def check_operator(_oper: str) -> bool:
    if len(_oper) != 1:
        return False

    return _oper == '+' or _oper == '-' or _oper == '*' or _oper == '/'


def calculate(_x: float, _y: float, _oper: str) -> float:
    if _oper == '+':
        return _x + _y
    if _oper == '-':
        return _x - _y
    if _oper == '*':
        return _x * _y
    if _oper == '/':
        return _x / _y


def is_one_digit(var: float) -> bool:
    return -10 < var < 10 and var.is_integer()


def check(_x: float, _y: float, _oper: str) -> str:
    msg = ''
    if is_one_digit(_x) and is_one_digit(_y):
        msg += ' ... lazy'
    if (_x == 1 or _y == 1) and _oper == '*':
        msg += ' ... very lazy'
    if (_x == 0 or _y == 0) and (_oper == '*' or _oper == '+' or _oper == '-'):
        msg += ' ... very, very lazy'
    if msg != '':
        msg = 'You are' + msg

    return msg


def store_or_not() -> bool:
    return input('Do you want to store the result? (y / n):') == 'y'


def calculate_or_not() -> bool:
    return input('Do you want to continue calculations? (y / n):') == 'y'


print('Enter an equation')
memory = 0
while True:
    try:
        x, oper, y = input().split()

        if x == 'M':
            x = memory
        if y == 'M':
            y = memory

        x, y = float(x), float(y)

        if not check_operator(oper):
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?\nEnter an equation")
        else:
            result_check = check(x, y, oper)
            if result_check != '':
                print(result_check)
            result = calculate(x, y, oper)
            print(result)
            answer_store = store_or_not()
            answer_calculate = calculate_or_not()
            if answer_store:
                memory = result
            if answer_calculate:
                print('Enter an equation')
                continue
            break

    except ValueError:
        print('Do you even know what numbers are? Stay focused!\nEnter an equation')
    except ZeroDivisionError:
        print('Yeah... division by zero. Smart move...\nEnter an equation')
