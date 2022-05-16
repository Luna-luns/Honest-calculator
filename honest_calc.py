def check_operator(_oper: str) -> bool:
    if len(_oper) != 1:
        return False

    return _oper == '+' or _oper == '-' or _oper == '*' or _oper == '/'


while True:
    try:
        print('Enter an equation')
        x, oper, y = input().split()

        float(x), float(y)

        if not check_operator(oper):
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        else:
            break

    except ValueError:
        print('Do you even know what numbers are? Stay focused!')
