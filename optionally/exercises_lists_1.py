# Создание списка:
# Создайте пустой список и добавьте в него 5 случайных целых чисел.

import random
random_list = []
i = 0

while (i != 5):
    random_number = random.randrange(1, 100)
    print(random_number)
    random_list.append(random_number)
    i = i+ 1
print (random_list)
