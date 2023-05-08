from telebot import TeleBot
from telebot.types import Message


def calculator_command(message: Message, bot: TeleBot) -> None:
    text = 'Здравствуй друг, это калькулятор в боте, пока что простейший, поддерживает 4 основых действия'

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)

    else:
        bot.reply_to(message, text)

    bot.user_dict['state'] = 'calculator'


def calculator_count(message: Message, bot: TeleBot) -> None:
    text_2 = 'Введи пример:(только цифры и +, -, *, /)'

    if message.chat.type == 'private':

        try:
            bot.send_message(message.from_user.id, eval(message.text))

        except Exception:
            bot.send_message(message.from_user.id, text_2)

        bot.send_message(message.from_user.id, eval(message.text))

    else:
        
        try:
            bot.reply_to(message, eval(message.text))

        except Exception:
            bot.reply_to(message, text_2)

        bot.reply_to(message, eval(message.text))
