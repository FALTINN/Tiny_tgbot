from telebot import TeleBot
from telebot.types import Message
from random import randint
import time
import sqlite3


def AddLength(message: Message, bot: TeleBot):
    connection = sqlite3.connect('C:\Code\Python\TelegramDB')
    cursor = connection.cursor()

    cursor.execute("SELECT Id_User from Loot")
    users = cursor.fetchall()
    cursor.execute("SELECT BaseId from Names")
    users2 = cursor.fetchall()


    if not(message.from_user.id in [user[0] for user in users]):
        cursor.execute("INSERT INTO Loot (Id_User, Length, TimeLastTake) VALUES (?, ?, ?)", (message.from_user.id, 0, 0))


    cursor.execute(f"SELECT Id from Loot where Id_User = {message.from_user.id}")
    Id = cursor.fetchall()


    if not(Id[0][0] in [user[0] for user in users2]):
        cursor.execute("INSERT INTO Names (BaseId, UserName) VALUES (?, ?)", (Id[0][0], message.from_user.full_name))


    cursor.execute(f"SELECT Names.UserName from Loot inner join Names on Loot.Id = Names.BaseId where Loot.Id_User = {message.from_user.id}")
    Name = cursor.fetchall()[0][0]


    if not(message.from_user.full_name == Name):
        cursor.execute("UPDATE Names SET UserName = (?) where Id = (?)", (message.from_user.full_name, Id[0][0]))

    
    cursor.execute(f"SELECT TimeLastTake from Loot where Id_User = {message.from_user.id}")
    
    if round(time.time()) - int(cursor.fetchall()[0][0]) >= 36000:
        cursor.execute(f"SELECT Length from Loot where Id_User = {message.from_user.id}")
        Added_number = randint(1, 10)
        Sum = Added_number + cursor.fetchall()[0][0]
        cursor.execute("UPDATE Loot SET Length = ?, TimeLastTake = ? where Id_User = ?", (Sum, round(time.time()), message.from_user.id))
        
        if message.chat.type == 'private':
            bot.send_message(message.from_user.id, f"Твоя писька увеличилась на {Added_number}см")

        else:
            bot.reply_to(message, f"{message.from_user.first_name}, твоя писька увеличилась на {Added_number}см")
    
    else:
        if message.chat.type == 'private':
            bot.send_message(message.from_user.id, "Подожди еще немного")

        else:
            bot.reply_to(message, "Подожди еще немного")

    connection.commit()
    connection.close()