# Telegram Bot for Expense Tracking

Этот Telegram-бот предназначен для учета расходов. Он позволяет пользователям добавлять, просматривать и удалять расходы с использованием базы данных SQLite.

## Функциональность
- Добавление нового расхода
- Просмотр всех расходов
- Удаление записей
- Интерактивное меню с кнопками

## Требования
- Python 3.12+
- Библиотеки: `aiogram`, `sqlite3`, `python-dotenv`

## Установка

1. **Склонировать репозиторий:**
```sh
git clone https://github.com/your-repo/telegram-expense-bot.git
cd telegram-expense-bot
```

2. **Создать виртуальное окружение и установить зависимости:**
```sh
python -m venv .venv
source .venv/bin/activate  # для Linux/macOS
.venv\Scripts\activate    # для Windows
pip install -r requirements.txt
```

3. **Создать файл `.env` и указать токен бота:**
```env
BOT_TOKEN=your_telegram_bot_token
```

4. **Запустить бота:**
```sh
python bot.py
```

## Использование
1. Открыть Telegram и найти своего бота.
2. Нажать `/start` для начала работы.
3. Использовать кнопки меню для добавления, просмотра и удаления расходов.

## Структура проекта
```
📂 telegram-expense-bot
│── bot.py          # Основной файл бота
│── database.py     # Работа с SQLite
│── handlers.py     # Обработчики команд
│── keyboards.py    # Клавиатуры
│── config.py       # Конфигурация бота
│── .env            # Переменные окружения (не коммитить!)
│── requirements.txt # Список зависимостей
```

## Лицензия
Этот проект распространяется под MIT лицензией.

