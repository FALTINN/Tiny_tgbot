from telebot import TeleBot
from telebot.types import Message


def get_text_messages_private(message: Message, bot: TeleBot) -> None:
    message_low = message.text.lower()
    if message_low == "привет":
        bot.send_message(message.from_user.id,
                         "Поставьте меня в ваш чат, сделайте администратором и я к вашим услугам")
    elif message_low == 'дурень':
        bot.send_message(message.from_user.id,
                    "!!!Ты поплатишься за это!!!")
    else:
        print('Correct', str(bot.get_state(message.from_user.id, message.chat.id)))
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
        bot.reply_to(message,
                         "Я тебя не понимаю. Напиши /help.")
