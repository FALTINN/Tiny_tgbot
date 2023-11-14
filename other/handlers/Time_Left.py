from telebot import TeleBot
from telebot.types import Message
import time
import sqlite3


def TimeLeft(message: Message, bot: TeleBot):
    connection = sqlite3.connect('C:\Code\Python\TelegramDB')
    cursor = connection.cursor()

    cursor.execute("SELECT Id_User from Loot")
    users = cursor.fetchall()

    if message.from_user.id in [ user[0] for user in users]:
        
        cursor.execute(f"SELECT TimeLastTake from Loot where Id_User = {message.from_user.id}")
        TimeLastTake = cursor.fetchall()[0][0]

        if TimeLastTake != 0 and (round(time.time() - TimeLastTake)) < 36000:
            Time = round(36000 - (time.time() - TimeLastTake))
            Time = f"{Time//3600}:{Time%3600//60}:{Time%3600%60}"
            
            if message.chat.type == 'private':
                bot.send_message(message.from_user.id, f"Времени до увеличения письки осталось {Time}")

            else:
                bot.reply_to(message, f"{message.from_user.first_name}, тебе осталось {Time} до увеличения письки")
        
        elif (round(time.time() - TimeLastTake)) > 36000 and TimeLastTake != 0:
            if message.chat.type == 'private':
                bot.send_message(message.from_user.id, f"Вы уже можете увеличить письку")

            else:
                bot.reply_to(message, f"{message.from_user.first_name}, Вы уже можете увеличить письку")

        else:
            if message.chat.type == 'private':
                bot.send_message(message.from_user.id, f"Вы ещё не увеличивали письку")

            else:
                bot.reply_to(message, f"{message.from_user.first_name}, Вы ещё не увеличивали письку")

    connection.commit()
    connection.close()