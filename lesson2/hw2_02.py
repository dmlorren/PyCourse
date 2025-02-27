# задание 2. Написать и вызвать функцию, принимающую два числа и возвращающую большее из двух.

def numbers_input(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input('введите первое число: '))
num2 = int(input('введите второе число: '))

print(f'большее число: {numbers_input(num1, num2)}')


#numbers_input()