# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число: '))
prodact = 1
print ('Произведений чисел от 1 до N: [', end='\t')
for i in range(1,N+1):
    prodact *= i 
    print (prodact, end='\t')
print (']', end='\t')