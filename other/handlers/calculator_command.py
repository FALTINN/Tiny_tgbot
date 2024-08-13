from telebot import TeleBot, types
from telebot.types import Message
from other.classes.MyState import MyState
from other.markups import cancel_keyboard
from other.handlers.stop_command import stop_command
from other.handlers.help_command import help_command_calculator
import math
from sympy import subfactorial


def calculator_command(message: Message, bot: TeleBot) -> None:
    text = 'Здравствуй друг, это калькулятор в боте, пока что простейший, поддерживает 6 основных действий\nВведи математические выражение и я выдам тебе ответ'

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text, reply_markup=cancel_keyboard)

    else:
        bot.reply_to(message, f'{text}. Чтобы выйти используйте команду stop или слово "назад". Чтобы узнать про возможности функции, используйте команду help_calculator или слово "помощь"')

    bot.set_state(message.from_user.id, MyState.Calculator, message.chat.id)
    print('Correct', bot.current_states.get_state(message.chat.id, message.from_user.id))


def calculator_count(message: Message, bot: TeleBot) -> None:
    text = 'Введи пример:(только цифры и +, -, *, /, !, ** и др.)'
    new_message = message.text.lower()

    if message.chat.type == 'private':

        try:
            if message.text[0] == '!' and int(message.text[1:]) < 100:
                bot.send_message(message.from_user.id, subfactorial(int(message.text[1:])), reply_markup=cancel_keyboard)

            elif message.text[len(message.text)-1] == '!':
                bot.send_message(message.from_user.id, math.factorial(int(message.text[:len(message.text)-1])), reply_markup=cancel_keyboard)

            elif new_message == 'назад':
                markup = types.ReplyKeyboardRemove()
                stop_command(message, bot)
                bot.send_message(message.from_user.id,"Вы вышли из калькулятора",reply_markup=markup)

            elif new_message == 'помощь':
                help_command_calculator(message, bot)

            else:
                bot.send_message(message.from_user.id, eval(message.text), reply_markup=cancel_keyboard)

        except:
            bot.send_message(message.from_user.id, text, reply_markup=cancel_keyboard)


    else:
        
        try:
            if message.text[0] == '!' and int(message.text[1:]) < 100:
                bot.reply_to(message, subfactorial(int(message.text[1:])))
            elif message.text[len(message.text)-1] == '!':
                bot.reply_to(message, math.factorial(int(message.text[:len(message.text)-1])))
            elif new_message == 'назад':
                stop_command(message, bot)
                bot.reply_to(message, 'Вы вышли из калькулятора')
            elif new_message == 'помощь':
                help_command_calculator(message, bot)
            else:
                bot.reply_to(message, eval(message.text))


        except:
            bot.reply_to(message, text)

