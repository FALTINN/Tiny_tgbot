from telebot import TeleBot, types
from telebot.types import Message
from other.classes.MyState import MyState
from other.handlers.stop_command import stop_command
from other.handlers.help_command import help_command_currency
from other.markups import value_keyboard
import requests


def command_exchange_rate(message: Message, bot: TeleBot):
    text = 'Узнайте курсы валют по данным ЦБ РФ'

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text, reply_markup=value_keyboard)

    else:
        bot.reply_to(message, f'{text}. Чтобы выйти используйте команду stop или слово "назад". Чтобы узнать про возможности функции, используйте команду help_currency или слово "помощь"')

    bot.set_state(message.from_user.id, MyState.ExchangeRate, message.chat.id)

def currency(message: Message, bot: TeleBot):
    currency = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    new_message = message.text.lower()
    if message.chat.type == 'private':
        
        if new_message == 'доллар':
            bot.send_message(message.from_user.id, f"Курс доллара по данным ЦБ на данный момент равен {round(currency['Valute']['USD']['Value'], 2)}₽")
        elif new_message == 'евро':
            bot.send_message(message.from_user.id, f"Курс евро по данным ЦБ на данный момент равен {round(currency['Valute']['EUR']['Value'], 2)}₽")
        elif new_message == 'фунт' or message.text == 'Фунт Стерлингов' or message.text == 'Британский Фунт':
            bot.send_message(message.from_user.id, f"Курс фунта стерлингов по данным ЦБ на данный момент равен {round(currency['Valute']['GBP']['Value'], 2)}₽")
        elif new_message == 'назад':
            markup = types.ReplyKeyboardRemove()
            stop_command(message, bot)
            bot.send_message(message.from_user.id,"Вы вышли из просмотра курса валют",reply_markup=markup)
        elif new_message == 'помощь':
            help_command_currency(message, bot)
        else:
            bot.send_message(message.from_user.id, "Что то не то")

    else:
        if new_message == 'доллар':
            bot.reply_to(message, f"Курс доллара по данным ЦБ на данный момент равен {round(currency['Valute']['USD']['Value'], 2)}₽")
        elif new_message == 'евро':
            bot.reply_to(message, f"Курс евро по данным ЦБ на данный момент равен {round(currency['Valute']['EUR']['Value'], 2)}₽")
        elif new_message == 'фунт' or message.text == 'Фунт Стерлингов' or message.text == 'Британский Фунт':
            bot.reply_to(message, f"Курс фунта стерлингов по данным ЦБ на данный момент равен {round(currency['Valute']['GBP']['Value'], 2)}₽")
        elif new_message == 'назад':
            stop_command(message, bot)
            bot.reply_to(message, 'Вы вышли из просмотра курса валют')
        elif new_message == 'помощь':
            help_command_currency(message, bot)
        else:
            bot.reply_to(message, "Что то не то")