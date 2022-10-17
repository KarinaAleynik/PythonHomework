# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]


ls = [1, 2, 3, 5, 1, 5, 3, 10]

res_unique = [i for i in ls if ls.count(i) == 1]

res_repeat = []
res_repeat_all = [i for i in ls if ls.count(i) == 2]
[res_repeat.append(i) for i in res_repeat_all if i not in res_repeat]


res_duplicate = []

[res_duplicate.append(i) for i in ls if i not in res_duplicate]


print(f'{res_unique} и {res_repeat} и {res_duplicate}')
