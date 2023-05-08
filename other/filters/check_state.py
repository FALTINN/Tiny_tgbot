from telebot.custom_filters import SimpleCustomFilter
from telebot.types import Message
from telebot import TeleBot


class checking_state(SimpleCustomFilter):
    key = 'state_user'

    def return_state(self, message: Message, bot: TeleBot) -> str:
        return bot.user_dict['state']