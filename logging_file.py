from aiogram import types
from datetime import datetime

def log_user(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    date_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open('user_log.txt', 'a') as f:
        f.write(f"{date_time} - {user_id} - {full_name} - {username}\n")

