# Обратная сортировка:
# Отсортируйте список целых чисел в порядке убывания.

def reverse_sort (lst):
    lst.sort(reverse=True)
    print(lst)

lst = [11, 14, 20, 69, -1, -20]

reverse_sort(lst)