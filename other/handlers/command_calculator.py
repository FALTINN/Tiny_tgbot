from telebot import TeleBot
from telebot.types import Message
from other.classes.MyState import MyState


def Factorial(number):
    if number == 1:
        return 1
    else:
        return number * Factorial(number - 1)
    

def SubFactorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 0
    else:
        return (number-1) * (SubFactorial(number-1) + SubFactorial(number-2))


def calculator_command(message: Message, bot: TeleBot) -> None:
    text = 'Здравствуй друг, это калькулятор в боте, пока что простейший, поддерживает 6 основных действий\nВведи математические выражение и я выдам тебе ответ'

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)

    else:
        bot.reply_to(message, text)

    bot.set_state(message.from_user.id, MyState.Calculator, message.chat.id)
    print('Correct', bot.current_states.get_state(message.chat.id, message.from_user.id))


def calculator_count(message: Message, bot: TeleBot) -> None:
    text_2 = 'Введи пример:(только цифры и +, -, *, /, !, **)'

    if message.chat.type == 'private':

        try:
            if message.text[0] == '!' and int(message.text[1:]) < 30:
                bot.send_message(message.from_user.id, SubFactorial(int(message.text[1:])))
            elif message.text[len(message.text)-1] == '!':
                bot.send_message(message.from_user.id, Factorial(int(message.text[:len(message.text)-1])))
            else:
                bot.send_message(message.from_user.id, eval(message.text))

        except Exception:
            bot.send_message(message.from_user.id, text_2)


    else:
        
        try:
            if message.text[0] == '!' and int(message.text[1:]) < 40:
                bot.reply_to(message, SubFactorial(int(message.text[1:])))
            elif message.text[len(message.text)-1] == '!':
                bot.reply_to(message, Factorial(int(message.text[:len(message.text)-1])))
            else:
                bot.reply_to(message, eval(message.text))


        except Exception:
            bot.reply_to(message, text_2)

