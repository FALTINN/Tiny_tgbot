from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


value_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
first_button = KeyboardButton('Доллар')
two_button = KeyboardButton('Евро')
third_button = KeyboardButton('Фунт Стерлингов')
fourth_button = KeyboardButton('Помощь')
fifth_button = KeyboardButton('Назад')
value_keyboard.add(first_button)
value_keyboard.add(two_button)
value_keyboard.add(third_button)
value_keyboard.add(fourth_button)
value_keyboard.add(fifth_button)

cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
first_button = KeyboardButton('Назад')
two_button = KeyboardButton('Помощь')
cancel_keyboard.add(first_button)
cancel_keyboard.add(two_button)
