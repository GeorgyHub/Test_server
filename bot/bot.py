# импорт нужных библиотек
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

# здесь храниться API-ключ бота
from config import TOKEN

# Заводские настройки
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Асинхронная функция сообщения
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello world!')

# Главная функция
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())