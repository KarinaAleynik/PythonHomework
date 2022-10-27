# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

import telebot

with open('bot_token2.txt', 'r') as file:
    token = file.read()


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    start_text = f'Привет, {message.from_user.first_name}! Что будем ' \
                 f'вычислять?\nВведите арифметическое выражение '
    bot.send_message(message.chat.id, start_text)


@bot.message_handler(content_types=['text'])
def eval_command(message):
    expression = message.text
    try:
        eval(expression)
    except (SyntaxError, NameError):
        bot.send_message(message.chat.id,
                         f'Выражение может содержать только числа и '
                         f'арифметические операторы.')
    else:
        bot.send_message(message.chat.id,
                         f'Результат равен:\n{eval(expression)}')


if __name__ == '__main__':
    bot.polling()
