from telebot import TeleBot
from telebot.types import Message

def version_command(message: Message, bot:TeleBot) -> None:
    text = '''Актуальная версия бота: 0.2.2
    В этой версии были пофикшены баги, добавлены новые фишки.'''

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)
    else:
        bot.reply_to(message, text)