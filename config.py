# -*- coding: utf-8 -*-
SITE_ADDRESS = "https://habrahabr.ru/rss/all/"
DB_NAME = "users.db"
BOT_TOKEN = "785639337:AAFbs7urnWipVsCeX9AuTmiMwLOd4i61ArY"
PROXY = 'https://190.104.8.19:3128'

COOLDOWN = 300  # in seconds

HELP_TEXT = '''Список команд:
	/my_tags - показать список тегов, на которые пользователь подписан
	/add_tags - добавить теги (пример: /add_tags IT Алгоритмы)
	/del_tags - удалить теги (пример: /del_tags IT Алгоритмы)
	/del_all_tags - удалить ВСЕ теги
	/copy_tags - скопировать теги из профиля на habr'e (пример: /copy_tags https://habr.ru/users/<user_name>/)
	/stop - приостановить рассылку (для продолжения рассылки - /start)

	Уточнения:
	1) Хаб = Тег
	2) Теги, которые должны быть удалены или добавлены, записываются через пробел
	3) Регистр тегов не важен
	4) Если пользователь не указал никаких тегов, то ему будут присылаться все статьи
	5) Если тег содержит пробелы, то они должны быть заменены на нижнее подчёркивание (Разработка под Windows -> Разработка_под_Windows)
	'''

ERROR_MESSAGE = "Упс, что-то пошло не так ¯\_(ツ)_/¯"
