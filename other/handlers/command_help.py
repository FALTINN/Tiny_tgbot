from telebot import TeleBot
from telebot.types import Message

def help_command(message: Message, bot: TeleBot) -> None:
    text = '''Команды в боте на данный момент:
     /help - отвечающая за вывод списка команд 
     /start- отвечающая за начало работы бота 
     /version - показывает актуальную версию и что в ней есть
     /calculator - считает числа, простейший калькулятор'''

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)
    else:
        bot.reply_to(message, text)