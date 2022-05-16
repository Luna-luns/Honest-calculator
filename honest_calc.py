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


print('Enter an equation')
while True:
    try:
        x, oper, y = input().split()

        float(x), float(y)

        if not check_operator(oper):
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?\nEnter an equation")
        else:
            print(calculate(float(x), float(y), oper))
            break

    except ValueError:
        print('Do you even know what numbers are? Stay focused!\nEnter an equation')
    except ZeroDivisionError:
        print('Yeah... division by zero. Smart move...\nEnter an equation')
