from telebot import TeleBot
from telebot.types import Message
from other.classes.MyState import MyState


def StopCommand(message: Message, bot: TeleBot):
    bot.delete_state(message.from_user.id, message.chat.id)