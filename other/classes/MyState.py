from telebot.handler_backends import State, StatesGroup


class MyState(StatesGroup):
    Calculator = State()
    ExchangeRate = State()
