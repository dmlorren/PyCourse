# Удаление дубликатов:
# Удалите дубликаты из списка, сохранив исходный порядок.

from collections import OrderedDict

def not_double_lst (lst):
    not_double = list(OrderedDict.fromkeys(lst))
    print(not_double)

lst = [11, 14, 20, 69, -1, -20, -1, 11, 4, 5, 3, 3]

not_double_lst(lst)