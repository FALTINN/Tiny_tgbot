from telebot import TeleBot
from telebot.types import Message
import sqlite3

from other import config


def get_top(message: Message, bot: TeleBot):
    connection = sqlite3.connect(config.path_to_db)
    cursor = connection.cursor()

    cursor.execute("""SELECT Names.UserName, Loot.Length 
                   FROM Loot INNER JOIN Names
                   ON Loot.id = Names.BaseId
                   ORDER BY Loot.Length DESC
                   LIMIT 5""")
    top = cursor.fetchall()
    text = f"""1. {top[0][0]} с длиной {top[0][1]}см
2. {top[1][0]} с длиной {top[1][1]}см
3. {top[2][0]} с длиной {top[2][1]}см
4. {top[3][0]} с длиной {top[3][1]}см
5. {top[4][0]} с длиной {top[4][1]}см"""

    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, text)

    else:
        bot.reply_to(message, text)

    connection.commit()
    connection.close()
