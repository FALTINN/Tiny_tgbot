from telebot import TeleBot
from telebot.types import Message


def get_text_messages_private(message: Message, bot: TeleBot) -> None:
    message_low = message.text.lower()
    if message_low == "привет":
        bot.send_message(message.from_user.id,
                         "Поставьте меня в ваш чат, сделайте администратором и я к вашим услугам")

    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")


def get_text_message_group(message: Message, bot: TeleBot) -> None:
    message_low = message.text.lower()
    if message_low == "привет":
        bot.reply_to(message,
                         "Привет, чем я могу тебе помочь?")
    elif message_low == 'дурень':
        bot.reply_to(message,
                    "!!!Ты поплатишься за это!!!")
    else:
        bot.send_message(message.chat.id,
                         "Я тебя не понимаю. Напиши /help.")
