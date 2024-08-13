from telebot import TeleBot
from telebot.types import Message
import sqlite3

from other import config


def get_length(message: Message, bot: TeleBot):
    connection = sqlite3.connect(config.path_to_db)
    cursor = connection.cursor()

    cursor.execute("SELECT Id_User from Loot")
    user_telegram_ids = cursor.fetchall()

    if not(message.from_user.id in [ user[0] for user in user_telegram_ids]):
        cursor.execute("INSERT INTO Loot (Id_User, Length, TimeLastTake) VALUES (?, ?, ?)", (message.from_user.id, 0, 0))
    
    cursor.execute(f"SELECT LENGTH from Loot where Id_User = {message.from_user.id}")
    length = cursor.fetchall()
    length = str(length[0][0])


    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, f"Твоя писька равна {length}см")

    else:
        bot.reply_to(message, f"{message.from_user.first_name}, твоя писька равна {length}см")

    connection.commit()
    connection.close()
