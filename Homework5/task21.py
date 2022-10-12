# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите исходный текст:  ").lower()


def del_words(my_text):
    my_text = list(filter(
        lambda x: 'а' not in x and 'б' not in x and 'в' not in x, my_text.split()))
    return " ".join(my_text)


print('Текст без слов, содержащих "а, б, в":  ', del_words(text))
