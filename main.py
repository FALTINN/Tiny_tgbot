from other.filters.check_the_chat_type import check_the_chat_type
from other.filters.check_state import checking_state

from other.handlers.chatting import get_text_message_group, get_text_messages_private
from other.handlers.command_start import start_command
from other.handlers.command_help import help_command
from other.handlers.command_version import version_command
from other.handlers.command_calculator import calculator_command
from other.handlers.command_calculator import calculator_count

from telebot import TeleBot
from other import config

class My_Bot(TeleBot):
    def __init__(self, config):
        self.user_dict = {
            'state': None
        }


if __name__ == '__main__':
    bot = My_Bot(config.token)

    # Добавляем свои фильтры
    bot.add_custom_filter(check_the_chat_type())
    bot.add_custom_filter(checking_state())

    # Регистрируем хэндлеры
    bot.register_message_handler(
        start_command, commands=['start'], pass_bot=True
    )
    bot.register_message_handler(
        calculator_command, commands=['calculator'], pass_bot=True
    )
    bot.register_message_handler(
        calculator_count, content_types=['text'], state_user='calculator', pass_bot=True
    )
    bot.register_message_handler(
        help_command, commands=['help'], pass_bot=True
    )
    bot.register_message_handler(
        version_command, commands=['version'], pass_bot=True
    )
    bot.register_message_handler(
        get_text_messages_private, content_types=['text'], chatType='private', pass_bot=True
    )
    bot.register_message_handler(
        get_text_message_group, content_types=['text'], chatType='group', pass_bot=True
    )

    bot.infinity_polling()

