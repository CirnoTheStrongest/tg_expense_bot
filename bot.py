import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from telegram import InputFile
from aiogram.filters import Command
from dotenv import load_dotenv
import database

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("secret"))
async def secret_handler(message: Message):
    await message.answer("Клевер - лучший кот! Мята - хуйня")

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я бот для учёта расходов. Напиши сумму, и я её сохраню.")

# Добавление расхода через команду "/add 250"
@dp.message(Command("add"))
async def add_expense_handler(message: Message):
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.answer("Используй формат: /add 250")
        return

    amount = float(args[1])
    database.add_expense(message.from_user.id, amount)
    await message.answer(f"Добавил расход: {amount} ₽")

# Получение статистики за сегодня
@dp.message(Command("stats"))
async def stats_handler(message: Message):
    total = database.get_today_expenses(message.from_user.id)
    await message.answer(f"Твои расходы за сегодня: {total} ₽")


# Команда "/list" — выводим все расходы с ID
@dp.message(Command("list"))
async def list_expenses_handler(message: Message):
    expenses = database.get_today_expenses_list(message.from_user.id)

    if not expenses:
        await message.answer("Нет расходов за сегодня.")
        return

    response = "Ваши расходы за сегодня:\n\n"
    for expense in expenses:
        response += f"ID: {expense[0]}, Сумма: {expense[1]} ₽, Категория: {expense[2]}, Дата: {expense[3]}\n"

    await message.answer(response)

# Удаление записи по ID через команду "/del <ID>"
@dp.message(Command("del"))
async def delete_expense_handler(message: Message):
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        await message.answer("Используй формат: /del <ID>")
        return

    expense_id = int(args[1])

    # Вызываем функцию из database.py для удаления
    database.delete_expense(expense_id)

    await message.answer(f"Запись с ID {expense_id} удалена!")

database.create_table()

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
