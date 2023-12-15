import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

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
    await message.answer(f"Привет, {message.from_user.first_name}!👋\n"
                         f"Я - {me.first_name} для определения выгодности покупки или продажи той"
                         f" или иной акции, с указанными параметрами!")


# Запуск процесса поллинга новых апдейтов
async def start_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
