# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.20

import random

lst = []

for i in range(lengh_lst := int(input("Введите длину списка: "))):
    lst.append(round(random.uniform(0,10),2))

print("Полученный список", lst)

min_element = lst[0] - int(lst[0])
max_element = lst[0] - int(lst[0])

for i in lst:
    if i - int(i) > max_element: max_element = i - int(i)
    elif i - int(i) < min_element: min_element = i - int(i)

print("Разница между максимальным и минимальным значением дробной части элементов", round(max_element-min_element, 2))