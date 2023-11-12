from telebot.custom_filters import AdvancedCustomFilter
from telebot.types import Message
from telebot import TeleBot
from telebot.handler_backends import State

from telebot import types


class checking_state(AdvancedCustomFilter):
    def __init__(self, bot: TeleBot):
        self.bot = bot

    key = 'state'

    def check(self, message, text):
        """
        :meta private:
        """
        print('State Check')
        if text == '*': return True
        
        # needs to work with callbackquery
        if isinstance(message, types.Message):
            chat_id = message.chat.id
            user_id = message.from_user.id

        if isinstance(message, types.CallbackQuery):
            
            chat_id = message.message.chat.id
            user_id = message.from_user.id
            message = message.message

        
        

        if isinstance(text, list):
            new_text = []
            for i in text:
                if isinstance(i, State): i = i.name
                new_text.append(i)
            text = new_text
        elif isinstance(text, State):
            text = text.name
        
        if message.chat.type in ['group', 'supergroup']:
            group_state = self.bot.current_states.get_state(chat_id, user_id)
            if group_state == text:
                return True
            elif type(text) is list and group_state in text:
                return True


        else:
            user_state = self.bot.current_states.get_state(chat_id, user_id)
            if user_state == text:
                return True
            elif type(text) is list and user_state in text:
                return True