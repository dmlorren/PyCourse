# Написать эхо-скрипт на Python,
# запрашивающий любые данные у пользователя и
# выводящий их с добавлением строки “Echo:” в начале.

#  f - позволяет вставлять значения переменных непосредственно в строку
# и не нужно указывать их через запятую

def echo_input():
    inf = input('Введите любую информацию: ')
    print(f'Echo: {inf}')

# вызов функции
echo_input()