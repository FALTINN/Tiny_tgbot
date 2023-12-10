from other.filters.check_the_chat_type import check_the_chat_type
from other.filters.check_state import checking_state

from other.handlers.chatting import get_text_message_group, get_text_messages_private
from other.handlers.command_start import start_command
from other.handlers.command_help import help_command
from other.handlers.command_version import version_command
from other.handlers.command_calculator import calculator_command
from other.handlers.command_calculator import calculator_count
from other.handlers.command_stop import StopCommand
from other.handlers.Add_Length import AddLength
from other.handlers.Get_Length import GetLength
from other.handlers.Time_Left import TimeLeft
from other.handlers.Get_Top import GetTop
from other.handlers.command_exchangeRate import commandExchangeRate, Currency
from other.classes.MyState import MyState

from telebot import TeleBot
from other import config
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage



if __name__ == '__main__':
    state_storage = StateMemoryStorage()
    bot = TeleBot(config.token, state_storage=state_storage)

    # Добавляем свои фильтры
    bot.add_custom_filter(checking_state(bot))
    bot.add_custom_filter(check_the_chat_type())


    # Регистрируем хэндлеры
    bot.register_message_handler(
        StopCommand, commands=['stop'], chatType='group', pass_bot=True
    )
    bot.register_message_handler(
        help_command, commands=['help'], pass_bot=True
    )
    bot.register_message_handler(
        calculator_command, commands=['calculator'], pass_bot=True
    )
    bot.register_message_handler(
        calculator_count, content_types=['text'], state=MyState.Calculator, pass_bot=True
    )
    bot.register_message_handler(
        commandExchangeRate, commands=['currency'], pass_bot=True
    )
    bot.register_message_handler(
        Currency, content_types=['text'], state=MyState.ExchangeRate, pass_bot=True
    )
    bot.register_message_handler(
        start_command, commands=['start'], pass_bot=True
    )
    bot.register_message_handler(
        version_command, commands=['version'], pass_bot=True
    )
    bot.register_message_handler(
        AddLength, commands=['add'], pass_bot=True
    )
    bot.register_message_handler(
        GetLength, commands=['get'], pass_bot=True
    )
    bot.register_message_handler(
        TimeLeft, commands=['time'], pass_bot=True
    )
    bot.register_message_handler(
        GetTop, commands=['top'], pass_bot=True
    )
    bot.register_message_handler(
        get_text_messages_private, content_types=['text'], chatType='private', pass_bot=True
    )
    bot.register_message_handler(
        get_text_message_group, content_types=['text'], chatType='group', pass_bot=True
    )

    bot.infinity_polling()

