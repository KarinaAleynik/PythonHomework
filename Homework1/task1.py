# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input("Введите цифру, обозначающую день недели: "))

if n > 7 or n <= 0: print("Нет дня недели соответствующей данной цифре")
elif n >= 6: print("Да")
else: print("Нет")