from aiogram import executor
import handlers

from bot import dp

async def on_startup(_):
    print('Бот запущен!!!')

if __name__ == '__main__':
    handlers.registred_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)