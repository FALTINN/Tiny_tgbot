from telebot.custom_filters import SimpleCustomFilter
from telebot.types import Message


class TheChatTypeChecker(SimpleCustomFilter):
    key = 'chatType'

    def check(self, message: Message) -> str:
        print('Chat Check')
        return message.chat.type
    