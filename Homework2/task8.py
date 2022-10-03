# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('Введите число N: '))

def sequence(n):

    return[round((1 + 1 / x)**x, 3) for x in range (1, n + 1)]   
        
print(sequence(n))
print(sum(sequence(n)))