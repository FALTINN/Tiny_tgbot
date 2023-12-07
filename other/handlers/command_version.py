from telebot import TeleBot
from telebot.types import Message

def version_command(message: Message, bot:TeleBot) -> None:
    text = '''Актуальная версия бота: 0.2.7
    Теперь команда stop не юзабельна для пользователя в одиночных чатах, исправлены уязвимости в коде. Исправлены баги'''

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)
    else:
        bot.reply_to(message, text)