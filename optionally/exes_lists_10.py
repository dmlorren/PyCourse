# Сдвиг элементов:
# Напишите функцию, которая сдвигает все элементы списка на одну позицию вправо.

#  это двусторонняя очередь в Python (ротор для моих данных)
from collections import deque

def func_lst (lst):
    deque_lst = deque(lst)
    # в скобках указано на сколько будем сдвигать
    deque_lst.rotate(1)
    # возвращаем индекс и значение после смещения на 1 позицию вправо
    for x in (enumerate(deque_lst)):
        print(f'---', x)

lst = [1,2,3,4,5]
func_lst(lst)

# #возвращаем индекс и значение для оригинального списка
# for i in (enumerate(lst)):
#     print(i)


