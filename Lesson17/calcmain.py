import calc
# from calc import add,mul,div,sub

class Calculator:
    def __init__(self):
        self.main()

    def main(self):
        print('Это калькулятор')
        while True:
            n1 = int(input('Первое число '))
            n2 = int(input('Второе число '))
            op = input('Введите знак действия, 0 - выход  ')
            match op:
                case '0':
                    break
                case '+':
                    print(calc.add(n1,n2))
                case '*':
                    print(calc.mul(n1, n2))
                case '-':
                    print(calc.sub(n1, n2))
                case '/':
                    print(calc.div(n1, n2))
                case _:
                    print('неверно')


if __name__=='__main__':
    a = Calculator()
