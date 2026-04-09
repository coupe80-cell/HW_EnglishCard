Чтобы запустить Telegram-бот необходимо выполнить:

1. Получить токен для Telegram-бота от BotFather в телеграмме.

2. Создать БД 

3. После выполнения пунктов 1 и 2 необходимо запонить полученными данными файл settings.ini как в примере:

[telegram]

token = "Вписать токен полученый от BotFather"

[postgres]

DSN = postgresql://postgres:password@localhost:5432/name_db

4. Запустите файл models.py для создания БД.

5. Запустите файл create_db.py он дабавит в основной словарь Telegram-бота несколько слов.

6. Запустите файл main.py для запуска Telegram-бота.
