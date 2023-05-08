from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)
one_button = KeyboardButton('Привет')
keyboard_1.add(one_button)