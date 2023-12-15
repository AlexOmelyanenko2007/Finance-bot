import asyncio
import logging
from contextlib import suppress

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher()


def get_start_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Выписать акции в ручную 🐾", callback_data="hand_data"),
            types.InlineKeyboardButton(text="Помощь 🙋‍", callback_data="help"),
            types.InlineKeyboardButton(text="История 👀‍", callback_data="history"),
        ],
        [types.InlineKeyboardButton(text="Из файла формата CSV", callback_data="csv_data")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    me = await bot.get_me()

    await message.answer(f"Привет, {message.from_user.first_name}!👋\n"
                         f"Я - {me.first_name} для определения выгодности покупки или продажи той"
                         f" или иной акции, с указанными параметрами!", reply_markup=get_start_keyboard())


@dp.callback_query(lambda c: c.data == "help")
async def answer_starting(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Вернуться в главное меню‍",
        callback_data="back_main_menu")
    )
    await callback.message.edit_text('Торговый бот - это бот, позволяющий'
                                     ' работать с данными о рынках, которые укажите для анализа с параметрами.'
                                     ' Благодаря чему бот примет решение по вашему вопросу и выдаст максимально '
                                     'выгодное предложение с использованием искусственного интеллекта 🤖.',
                                     reply_markup=builder.as_markup())


@dp.callback_query(lambda c: c.data == "back_main_menu")
async def back_main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text('Чем я еще могу помочь?', reply_markup=get_start_keyboard())


@dp.message(F.text)
async def unknown_text_reply(message: types.Message):
    text = message.text
    msg = await message.answer("Неизвестная команда.")
    await asyncio.sleep(3.5)
    await msg.delete()
    await message.delete()

async def start_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
