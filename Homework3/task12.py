# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

lst = []

for i in range(lengh_lst := int(input("Введите длину списка: "))):
    lst.append(random.randint(-10, 10))

print("Полученный список", lst)

lst_product = []

if lengh_lst % 2:
    for i in range(lengh_lst//2 + 1):
        lst_product.append(lst[i] * lst[-i-1])
else:
    for i in range(lengh_lst//2):
        lst_product.append(lst[i] * lst[-i-1])

print('Произведение пар чисел списка ', lst_product)
