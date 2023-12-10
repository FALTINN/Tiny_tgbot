from telebot import TeleBot, types
from telebot.types import Message
from other.classes.MyState import MyState
from other.handlers.command_stop import StopCommand
from other.markups import Valute_keyboard
import requests


def commandExchangeRate(message: Message, bot: TeleBot):
    text = 'Узнайте курсы валют по данным ЦБ РФ'

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text, reply_markup=Valute_keyboard)

    else:
        bot.reply_to(message, f'{text}. Чтобы выйти используйте команду stop или слово "назад"')

    bot.set_state(message.from_user.id, MyState.ExchangeRate, message.chat.id)

def Currency(message: Message, bot: TeleBot):
    currency = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    newMessage = message.text.lower()
    if message.chat.type == 'private':
        
        if newMessage == 'доллар':
            bot.send_message(message.from_user.id, f"Курс доллара по данным ЦБ на данный момент равен {round(currency['Valute']['USD']['Value'], 2)}₽")
        elif newMessage == 'евро':
            bot.send_message(message.from_user.id, f"Курс евро по данным ЦБ на данный момент равен {round(currency['Valute']['EUR']['Value'], 2)}₽")
        elif newMessage == 'фунт' or message.text == 'Фунт Стерлингов' or message.text == 'Британский Фунт':
            bot.send_message(message.from_user.id, f"Курс фунта стерлингов по данным ЦБ на данный момент равен {round(currency['Valute']['GBP']['Value'], 2)}₽")
        elif newMessage == 'назад':
            markup = types.ReplyKeyboardRemove()
            StopCommand(message, bot)
            bot.send_message(message.from_user.id,"Вы вышли из просмотра курса валют",reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, "Что то не то")

    else:
        if newMessage == 'доллар':
            bot.reply_to(message, f"Курс доллара по данным ЦБ на данный момент равен {round(currency['Valute']['USD']['Value'], 2)}₽")
        elif newMessage == 'евро':
            bot.reply_to(message, f"Курс евро по данным ЦБ на данный момент равен {round(currency['Valute']['EUR']['Value'], 2)}₽")
        elif newMessage == 'фунт' or message.text == 'Фунт Стерлингов' or message.text == 'Британский Фунт':
            bot.reply_to(message, f"Курс фунта стерлингов по данным ЦБ на данный момент равен {round(currency['Valute']['GBP']['Value'], 2)}₽")
        elif newMessage == 'назад':
            StopCommand(message, bot)
            bot.reply_to(message, 'Вы вышли из просмотра курса валют')
        else:
            bot.reply_to(message, "Что то не то")