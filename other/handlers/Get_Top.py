from telebot import TeleBot
from telebot.types import Message
import sqlite3


def GetTop(message: Message, bot: TeleBot):
    connection = sqlite3.connect('C:\Code\Python\TelegramDB')
    cursor = connection.cursor()

    cursor.execute("""SELECT Names.UserName, Loot.Length 
                   FROM Loot INNER JOIN Names
                   ON Loot.id = Names.BaseId
                   ORDER BY Loot.Length DESC
                   LIMIT 5""")
    Top = cursor.fetchall()
    Text = f"""1. {Top[0][0]} с длиной {Top[0][1]}см
2. {Top[1][0]} с длиной {Top[1][1]}см
3. {Top[2][0]} с длиной {Top[2][1]}см
4. {Top[3][0]} с длиной {Top[3][1]}см
5. {Top[4][0]} с длиной {Top[4][1]}см"""
    
    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, Text)

    else:
        bot.reply_to(message, Text)


    connection.commit()
    connection.close()