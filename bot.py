import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    me = await bot.get_me()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Помощь 🙋‍",
        callback_data="help")
    )

    await message.answer(f"Привет, {message.from_user.first_name}!👋\n"
                         f"Я - {me.first_name} для определения выгодности покупки или продажи той"
                         f" или иной акции, с указанными параметрами!", reply_markup=builder.as_markup())


@dp.callback_query(lambda c: c.data == "help")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer('Торговый бот - это бот, позволяющий'
                                  ' работать с данными о рынках, которые укажите для анализа с параметрами.'
                                  ' Благодаря чему бот примет решение по вашему вопросу и выдаст максимально выгодное'
                                  ' предложение с использованием искусственного интеллекта 🤖.')


async def start_bot():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(start_bot())
