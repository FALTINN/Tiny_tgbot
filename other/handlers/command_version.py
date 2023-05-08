from telebot import TeleBot
from telebot.types import Message

def version_command(message: Message, bot:TeleBot) -> None:
    text = '''Актуальная версия бота: 0.1.1
    В этой версии обновлена работа некоторых команд, изменены небольшие мелочи
    И...... Добавлен калькулятор(хоть и простейший)'''

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)
    else:
        bot.reply_to(message, text)