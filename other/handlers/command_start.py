from telebot import TeleBot
from telebot.types import Message
from random import choice


def start_command(message: Message, bot: TeleBot) -> None:
    the_newcomer = choice(['Здравствуй путник', 'Приветствую', 'Рад вас видеть', 'Добро пожаловать в GYM', 'Приветствуем в МэйбиЛенде'])
    text = f'{the_newcomer}, <b>{message.from_user.first_name}</b>!'

    if message.chat.type == 'private':
        bot.send_message(message.chat.id, text, parse_mode='HTML')
    else:
        bot.reply_to(message, text, parse_mode='HTML')
