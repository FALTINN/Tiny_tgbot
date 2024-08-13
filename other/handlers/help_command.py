from telebot import TeleBot
from telebot.types import Message

def help_command(message: Message, bot: TeleBot) -> None:
    text = '''Команды в боте на данный момент:
     /help - показывает актуальные команды
     /help_currency - покавает какие курсы валют можно узнать
     /help_calculator - показывает возможности калькулятора
     /start- отвечает за начало работы бота 
     /version - показывает актуальную версию и что в ней есть
     /calculator - считает числа, простейший калькулятор
     /stop - выйти из зацикленных функций(только для групп)
     /add - увеличить письку
     /get - узнать длину письки
     /time - узнать время до увеличения письки
     /top - показывает топ игроков
     /currency - узнать нынешний курс'''

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)
    else:
        bot.reply_to(message, text)


def help_command_calculator(message: Message, bot: TeleBot):
    text = """Бот поддерживает базовые операции(+, -, *)
    Также несколько видов делений: С остатком(/), Без остатка(//), Получение остатка(%)
    Возведение в степень(**)
    Получение факториала(! после выражения), субфакториала(! перед выражением)
    Получение квадратного корня(**0.5)"""

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)
    else:
        bot.reply_to(message, text)


def help_command_currency(message: Message, bot: TeleBot):
    text = """Ты можешь получить курс таких валют, как:
    Доллар
    Евро
    Фунт Стерлингов"""

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)
    else:
        bot.reply_to(message, text)