def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    if n2==0:
        return 'Нельзя делить на ноль'
    return n1/n2

print('Это калькулятор')

if __name__=='__main__':
    while True:
        n1 = int(input('Первое число '))
        n2 = int(input('Второе число '))
        op = input('Введите знак действия, 0 - выход  ')
        match op:
            case '0':
                break
            case '+':
                print(add(n1, n2))
            case '*':
                print(mul(n1, n2))
            case '-':
                print(sub(n1, n2))
            case '/':
                print(div(n1, n2))
            case _:
                print('неверно')


