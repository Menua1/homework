from aiogram import Dispatcher
import view

def registred_handlers(dp: Dispatcher):
  dp.register_message_handler(view.cmd_start, commands=['start'])