from telebot import TeleBot
from telebot.types import Message
from random import randint
import sqlite3


def GetLength(message: Message, bot: TeleBot):
    connection = sqlite3.connect('C:\Code\Python\TelegramDB')
    cursor = connection.cursor()

    cursor.execute("SELECT Id_User from Loot")
    users = cursor.fetchall()

    if not(message.from_user.id in [ user[0] for user in users]):
        cursor.execute("INSERT INTO Loot (Id_User, Length, TimeLastTake) VALUES (?, ?, ?)", (message.from_user.id, 0, 0))
    
    cursor.execute(f"SELECT LENGTH from Loot where Id_User = {message.from_user.id}")
    Length = cursor.fetchall()
    Length = str(Length[0][0])


    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, f"Твоя писька равна {Length}см")

    else:
        bot.reply_to(message, f"{message.from_user.first_name}, твоя писька равна {Length}см")

    connection.commit()
    connection.close()
