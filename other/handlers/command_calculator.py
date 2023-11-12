from telebot import TeleBot
from telebot.types import Message
from other.classes.MyState import MyState



def calculator_command(message: Message, bot: TeleBot) -> None:
    text = 'Здравствуй друг, это калькулятор в боте, пока что простейший, поддерживает 4 основых действия/nВведи математические выражение и я выдам тебе ответ'

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)

    else:
        bot.reply_to(message, text)

    bot.set_state(message.from_user.id, MyState.Calculator, message.chat.id)
    print('Correct', bot.current_states.get_state(message.chat.id, message.from_user.id))


def calculator_count(message: Message, bot: TeleBot) -> None:
    print("Success")
    text_2 = 'Введи пример:(только цифры и +, -, *, /)'

    if message.chat.type == 'private':

        try:
            bot.send_message(message.from_user.id, eval(message.text))

        except Exception:
            bot.send_message(message.from_user.id, text_2)


    else:
        
        try:
            bot.reply_to(message, eval(message.text))

        except Exception:
            bot.reply_to(message, text_2)

