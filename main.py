from other.filters.TheChatTyperChecker import TheChatTypeChecker
from other.filters.StateChecker import StateChecker

from other.handlers.chatting import get_text_message_group, get_text_messages_private
from other.handlers.start_command import start_command
from other.handlers.help_command import help_command, help_command_calculator, help_command_currency
from other.handlers.version_command import version_command
from other.handlers.calculator_command import calculator_command, calculator_count
from other.handlers.stop_command import stop_command
from other.handlers.add_length_command import add_length
from other.handlers.get_length_command import get_length
from other.handlers.get_time_left_command import get_time_left
from other.handlers.get_top_command import get_top
from other.handlers.exchange_rate_command import command_exchange_rate, currency
from other.classes.MyState import MyState

from telebot import TeleBot
from other import config
from telebot.storage import StateMemoryStorage

if __name__ == '__main__':
    state_storage = StateMemoryStorage()
    bot = TeleBot(config.token, state_storage=state_storage)

    # Добавляем свои фильтры
    bot.add_custom_filter(StateChecker(bot))
    bot.add_custom_filter(TheChatTypeChecker())

    # Регистрируем хэндлеры
    bot.register_message_handler(
        stop_command, commands=['stop'], chatType='group', pass_bot=True
    )
    bot.register_message_handler(
        help_command, commands=['help'], pass_bot=True
    )
    bot.register_message_handler(
        calculator_command, commands=['calculator'], state=None, pass_bot=True
    )
    bot.register_message_handler(
        help_command_calculator, commands=['help_calculator'], state=MyState.Calculator, pass_bot=True
    )
    bot.register_message_handler(
        calculator_count, content_types=['text'], state=MyState.Calculator, pass_bot=True
    )
    bot.register_message_handler(
        command_exchange_rate, commands=['currency'], state=None, pass_bot=True
    )
    bot.register_message_handler(
        help_command_currency, commands=['help_currency'], state=MyState.ExchangeRate, pass_bot=True
    )
    bot.register_message_handler(
        currency, content_types=['text'], state=MyState.ExchangeRate, pass_bot=True
    )
    bot.register_message_handler(
        start_command, commands=['start'], pass_bot=True
    )
    bot.register_message_handler(
        version_command, commands=['version'], pass_bot=True
    )
    bot.register_message_handler(
        add_length, commands=['add'], pass_bot=True
    )
    bot.register_message_handler(
        get_length, commands=['get'], pass_bot=True
    )
    bot.register_message_handler(
        get_time_left, commands=['time'], pass_bot=True
    )
    bot.register_message_handler(
        get_top, commands=['top'], pass_bot=True
    )
    bot.register_message_handler(
        get_text_messages_private, content_types=['text'], chatType='private', pass_bot=True
    )
    bot.register_message_handler(
        get_text_message_group, content_types=['text'], chatType='group', pass_bot=True
    )

    bot.infinity_polling()
