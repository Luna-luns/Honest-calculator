def is_number(_x: str, _y: str) -> bool:
    return not _x.isalpha() and not _y.isalpha()


def check_operator(_oper: str) -> bool:
    if len(_oper) != 1:
        return False

    return _oper == '+' or _oper == '-' or _oper == '*' or _oper == '/'


while True:
    print('Enter an equation')
    x, oper, y = input().split()
    if not is_number(x, y):
        print('Do you even know what numbers are? Stay focused!')
    else:
        if not check_operator(oper):
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        else:
            break
