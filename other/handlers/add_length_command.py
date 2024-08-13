from telebot import TeleBot
from telebot.types import Message
from random import randint
import time
import sqlite3

from other import config


def add_length(message: Message, bot: TeleBot):
    connection = sqlite3.connect(config.path_to_db)
    cursor = connection.cursor()

    cursor.execute("SELECT Id_User from Loot")
    user_telegram_ids = cursor.fetchall()
    cursor.execute("SELECT BaseId from Names")
    uses_bot_ids = cursor.fetchall()


    if not(message.from_user.id in [user[0] for user in user_telegram_ids]):
        cursor.execute("INSERT INTO Loot (Id_User, Length, TimeLastTake) VALUES (?, ?, ?)", (message.from_user.id, 0, 0))


    cursor.execute(f"SELECT Id from Loot where Id_User = {message.from_user.id}")
    id = cursor.fetchall()


    if not(id[0][0] in [user[0] for user in uses_bot_ids]):
        cursor.execute("INSERT INTO Names (BaseId, UserName) VALUES (?, ?)", (id[0][0], message.from_user.full_name))


    cursor.execute(f"SELECT Names.UserName from Loot inner join Names on Loot.Id = Names.BaseId where Loot.Id_User = {message.from_user.id}")
    name = cursor.fetchall()[0][0]


    if not(message.from_user.full_name == name):
        cursor.execute("UPDATE Names SET UserName = (?) where Id = (?)", (message.from_user.full_name, id[0][0]))

    
    cursor.execute(f"SELECT TimeLastTake from Loot where Id_User = {message.from_user.id}")
    
    if round(time.time()) - int(cursor.fetchall()[0][0]) >= 36000:
        cursor.execute(f"SELECT Length from Loot where Id_User = {message.from_user.id}")
        added_number = randint(1, 10)
        sum = added_number + cursor.fetchall()[0][0]
        cursor.execute("UPDATE Loot SET Length = ?, TimeLastTake = ? where Id_User = ?", (sum, round(time.time()), message.from_user.id))
        
        if message.chat.type == 'private':
            bot.send_message(message.from_user.id, f"Твоя писька увеличилась на {added_number}см")

        else:
            bot.reply_to(message, f"{message.from_user.first_name}, твоя писька увеличилась на {added_number}см")
    
    else:
        if message.chat.type == 'private':
            bot.send_message(message.from_user.id, "Подожди еще немного")

        else:
            bot.reply_to(message, "Подожди еще немного")

    connection.commit()
    connection.close()
