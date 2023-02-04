import random
from aiogram import types
from bot import bot, dp
from logging_file import log_user

# Старт игры
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    log_user(message)
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("➡ Начать ⬅", callback_data="start")
    keyboard.add(button)

    await bot.send_message(chat_id=message.chat.id, text="💥<b>Правило игры:</b>💥\n\n"
                                                         "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯\n\n"
                                                         "На столе есть определенное количество  🍩  \n\n"
                                                         "Играют два игрока, делая ход друг за другом. \n\n"
                                                         "Первый ход определяется путем жеребьевки. \n\n"
                                                         "За один ход вы можете взять определенной количество 🍩 \n\n"
                                                         "Все 🍩 противника достаются тому, кто сделал последний ход.\n\n",
                           reply_markup=keyboard, parse_mode="html")

# Начало игры
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'start')
async def process_callback_start(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text=f"{callback_query.from_user.username}! Давайте играть!")

    keyboard = types.InlineKeyboardMarkup()
    button_play = types.InlineKeyboardButton("✅  Играть", callback_data="play")
    button_exit = types.InlineKeyboardButton("❌  Выход", callback_data="exit")
    keyboard.add(button_play)
    keyboard.add(button_exit)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f"➡ {callback_query.from_user.username}! Начать игру ❓ ⬅", reply_markup=keyboard)

# Выход из игры
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'exit')
async def process_callback_exit(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text=f"{callback_query.from_user.username}! До свидания!")

    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Начать", callback_data="start")
    keyboard.add(button)

    await bot.send_message(chat_id=callback_query.message.chat.id, text="💥<b>Правило игры:</b>💥\n\n"
                                                                        "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯\n\n"
                                                                        "На столе есть определенное количество  🍩  \n\n"
                                                                        "Играют два игрока, делая ход друг за другом. \n\n"
                                                                        "Первый ход определяется путем жеребьевки. \n\n"
                                                                        "За один ход вы можете взять определенной количество 🍩 \n\n"
                                                                        "Все 🍩 противника достаются тому, кто сделал последний ход.\n\n",
                           reply_markup=keyboard, parse_mode="html")

# Выбор общего количества
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'play')
async def selecting_total_quantity(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text=f"{callback_query.from_user.username}! Игра началась!")

    keyboard = types.InlineKeyboardMarkup()
    button_140_159 = types.InlineKeyboardButton("140 ➖ 159", callback_data="140_159")
    button_160_179 = types.InlineKeyboardButton("160 ➖ 179", callback_data="160_179")
    button_180_200 = types.InlineKeyboardButton("180 ➖ 200", callback_data="180_200")
    keyboard.add(button_140_159)
    keyboard.add(button_160_179)
    keyboard.add(button_180_200)
    await bot.send_message(chat_id=callback_query.message.chat.id, text="➡Выберите общее количество конфет 🍩 ⬅",
                           reply_markup=keyboard)

# Гениратор случайного число  общего количества
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['140_159', '160_179', '180_200'])
async def random_total_number(callback_query: types.CallbackQuery):
    global total_candies

    selected_range = callback_query.data
    if selected_range == '140_159':
        total_candies = random.randint(140, 159)

    elif selected_range == '160_179':
        total_candies = random.randint(160, 179)

    else:
        total_candies = random.randint(180, 200)

    await bot.answer_callback_query(callback_query.id,
                                    text=f"{callback_query.from_user.username}! Выбрал {total_candies} 🍩")
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f"➡ Общее количество 🍩 на столе 🟰 {total_candies} ⬅")

    keyboard = types.InlineKeyboardMarkup()
    button_15_19 = types.InlineKeyboardButton("15 ➖ 19", callback_data="15_19")
    button_20_24 = types.InlineKeyboardButton("20 ➖ 24", callback_data="20_24")
    button_25_30 = types.InlineKeyboardButton("25 ➖ 30", callback_data="25_30")
    keyboard.add(button_15_19)
    keyboard.add(button_20_24)
    keyboard.add(button_25_30)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="➡  Выберите максимальную количество 🍩 за один ход ⬅", reply_markup=keyboard)

# Гениратор случаного максимального числа, которое может взять игрок
@dp.callback_query_handler(lambda callback_query: callback_query.data in ['15_19', '20_24', '25_30'])
async def random_max_number(callback_query: types.CallbackQuery):
    global max_candies, total_candies

    selected_range = callback_query.data
    if selected_range == '15_19':
        max_candies = random.randint(15, 19)

    elif selected_range == '20_24':
        max_candies = random.randint(20, 24)

    else:
        max_candies = random.randint(25, 30)

    await bot.answer_callback_query(callback_query.id,
                                    text=f"{callback_query.from_user.username} выбрал {max_candies} 🍩")
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f"➡ Максимальное  количество 🍩 за один ход, которые могут быть взяты 🟰 {max_candies} ⬅")

    keyboard = types.InlineKeyboardMarkup()
    button_first_move = types.InlineKeyboardButton("Кто пойдет первым ❓", callback_data="first_move")
    keyboard.add(button_first_move)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text=f"Общее количество 🍩 на столе 🟰 {total_candies}.\n\n"
                                f"Максимальное количество 🍩 за один ход 🟰 {max_candies}.\n\n"
                                f"Чтобы определить, кто берет 🍩 первым, нажмите на кнопку ниже", reply_markup=keyboard)

# Гениратор случайного числа кто будет ходить первым, игра с ботом, первый ход бота
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'first_move')
async def random_first_move(callback_query: types.CallbackQuery):
    global max_candies, total_candies, first_move

    first_move = random.randint(1, 2)

    if first_move == 1:

        await bot.answer_callback_query(callback_query.id,
                                        text=f"➡ {callback_query.from_user.username}! Ты берешь 🍩 первым!⬅")

        buttons = []
        for i in range(1, min(total_candies + 1, 31)):
            button = types.InlineKeyboardButton(str(i), callback_data=str(i))
            buttons.append(button)
        keyboard = types.InlineKeyboardMarkup(row_width=6)
        keyboard.add(*buttons)

        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=f"➡ Ты берешь 🍩 первым! Выберите число от 1 до {max_candies} ⬅",
                               reply_markup=keyboard)

    else:
        await bot.answer_callback_query(callback_query.id, text=f"{callback_query.from_user.username}! 🐵 берет первая!")
        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=f"➡ {callback_query.from_user.username}! 🐵 берет первая ⬅")

        bot_move = total_candies % (max_candies + 1) if total_candies % (max_candies + 1) != 0 else random.randint(1, (
                    max_candies + 1))
        total_candies -= bot_move

        if total_candies == 0:
            await bot.send_message(chat_id=callback_query.message.chat.id,
                                   text=f"➡ 🐵 взяла последний 🍩! 🐵 выиграла игру! ⬅")
            return

        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=f"➡ 🐵 взяла {bot_move} 🍩. На столе осталось {total_candies} 🍩. Ваша очередь, выберите число от 1 до {max_candies}⬅")

        buttons = []
        for i in range(1, min(total_candies + 1, 31)):
            button = types.InlineKeyboardButton(str(i), callback_data=str(i))
            buttons.append(button)
        keyboard = types.InlineKeyboardMarkup(row_width=6)
        keyboard.add(*buttons)

        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=f"➡ Ваша очередь, выберите число от 1 до {max_candies} ⬅", reply_markup=keyboard)

# Игра с ботом, первый ход игрока
@dp.callback_query_handler(lambda callback_query: callback_query.data in [str(i) for i in range(1, 31)])
async def playing_with_bot(callback_query: types.CallbackQuery):
    global max_candies, first_move, total_candies

    selected_number = int(callback_query.data)

    if selected_number > max_candies:
        await bot.answer_callback_query(callback_query.id,
                                        text=f"➡ {callback_query.from_user.username}! Повторите попытку, возьмите от 1 до {max_candies} ⬅")

    else:
        total_candies -= selected_number

        if total_candies == 0:
            await bot.send_message(chat_id=callback_query.message.chat.id,
                                   text=f"➡ {callback_query.from_user.username}, ты взял последний 🍩! Ты выиграл игру! ⬅")
            return

        await bot.answer_callback_query(callback_query.id, text=f"{callback_query.from_user.username}! ты взял {selected_number} 🍩.")
        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=f"➡ {callback_query.from_user.username}, ты взял {selected_number} 🍩. Осталось {total_candies} 🍩 . Очередь 🐵! ⬅")

        bot_move = total_candies % (max_candies + 1) if total_candies % (max_candies + 1) != 0 else random.randint(1, (
                    max_candies + 1))
        total_candies -= bot_move

        if total_candies == 0:
            await bot.send_message(chat_id=callback_query.message.chat.id,
                                   text=f"➡ 🐵 забрал последний 🍩! 🐵 выиграла игру! ⬅")
            return

        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=f"➡ {callback_query.from_user.username}, 🐵 взяла {bot_move} 🍩. Осталось {total_candies} 🍩 . Ваша очередь, выберите число от 1 до {max_candies} ⬅")

        buttons = []
        for i in range(1, min(total_candies + 1, 31)):
            button = types.InlineKeyboardButton(str(i), callback_data=str(i))
            buttons.append(button)
        keyboard = types.InlineKeyboardMarkup(row_width=6)
        keyboard.add(*buttons)
        await bot.send_message(chat_id=callback_query.message.chat.id,
                               text=f"➡ Ваша очередь, выберите число от 1 до {max_candies} ⬅", reply_markup=keyboard)