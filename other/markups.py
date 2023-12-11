from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


Valute_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
one_button = KeyboardButton('Доллар')
two_button = KeyboardButton('Евро')
three_button = KeyboardButton('Фунт Стерлингов')
four_button = KeyboardButton('Помощь')
five_button = KeyboardButton('Назад')
Valute_keyboard.add(one_button)
Valute_keyboard.add(two_button)
Valute_keyboard.add(three_button)
Valute_keyboard.add(four_button)
Valute_keyboard.add(five_button)

Cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
one_button = KeyboardButton('Назад')
two_button = KeyboardButton('Помощь')
Cancel_keyboard.add(one_button)
Cancel_keyboard.add(two_button)