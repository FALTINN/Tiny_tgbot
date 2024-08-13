from telebot import TeleBot
from telebot.types import Message
import time
import sqlite3
from dateutil.parser import parse

from other import config


def get_time_left(message: Message, bot: TeleBot):
    connection = sqlite3.connect(config.path_to_db)
    cursor = connection.cursor()

    cursor.execute("SELECT Id_User from Loot")
    user_telegram_ids = cursor.fetchall()

    if message.from_user.id in [user[0] for user in user_telegram_ids]:
        
        cursor.execute(f"SELECT TimeLastTake from Loot where Id_User = {message.from_user.id}")
        time_last_take = cursor.fetchall()[0][0]

        if time_last_take != 0 and (round(time.time() - time_last_take)) < 36000:
            Time = round(36000 - (time.time() - time_last_take))
            Time = f"{Time//3600}:{Time%3600//60}"
            Time = str(parse(Time).time())
            Time = Time[:len(Time)-3]
               
            if message.chat.type == 'private':
                bot.send_message(message.from_user.id, f"Времени до увеличения письки осталось {Time}")

            else:
                bot.reply_to(message, f"{message.from_user.first_name}, тебе осталось {Time} до увеличения письки")
        
        elif (round(time.time() - time_last_take)) > 36000 and time_last_take != 0:
            if message.chat.type == 'private':
                bot.send_message(message.from_user.id, "Вы уже можете увеличить письку")

            else:
                bot.reply_to(message, f"{message.from_user.first_name}, Вы уже можете увеличить письку")

        else:
            if message.chat.type == 'private':
                bot.send_message(message.from_user.id, "Вы ещё не увеличивали письку")

            else:
                bot.reply_to(message, f"{message.from_user.first_name}, Вы ещё не увеличивали письку")
    else:
        if message.chat.type == 'private':
            bot.send_message(message.from_user.id, "Вы еще не зарегистрированы")

        else:
            bot.reply_to(message, f"{message.from_user.first_name}, Вы ещё не зарегистрированы")

    connection.commit()
    connection.close()
