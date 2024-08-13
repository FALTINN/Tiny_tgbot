from telebot import TeleBot
from telebot.types import Message


def stop_command(message: Message, bot: TeleBot):
    bot.delete_state(message.from_user.id, message.chat.id)
