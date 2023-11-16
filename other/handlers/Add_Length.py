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

    if not(message.from_user.id in [ user[0] for user in users]):
        cursor.execute("INSERT INTO Loot (Id_User, Length, TimeLastTake) VALUES (?, ?, ?)", (message.from_user.id, 0, 0))
    
    cursor.execute(f"SELECT TimeLastTake from Loot where Id_User = {message.from_user.id}")
    if round(time.time()) - int(cursor.fetchall()[0][0]) >= 36000:
        cursor.execute(f"SELECT Length from Loot where Id_User = {message.from_user.id}")
        Added_number = randint(1, 10)
        Sum = Added_number + cursor.fetchall()[0][0]
        cursor.execute("UPDATE Loot SET Length = ?, TimeLastTake = ? where Id_User = ?", (Sum, round(time.time()), message.from_user.id))

        if Added_number == 1: Centimeter = "сантиметр"
        elif Added_number >= 2 and Added_number <= 4: Centimeter = "сантиметра"
        else: Centimeter = "сантиметров"
        
        if message.chat.type == 'private':
            bot.send_message(message.from_user.id, f"Твоя писька увеличилась на {Added_number} {Centimeter}")

        else:
            bot.reply_to(message, f"{message.from_user.first_name}, твоя писька увеличилась на {Added_number} {Centimeter}")
    else:
        if message.chat.type == 'private':
            bot.send_message(message.from_user.id, "Подожди еще немного")

        else:
            bot.reply_to(message, "Подожди еще немного")

    connection.commit()
    connection.close()