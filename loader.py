from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

#  Логгирование в боте является важным инструментом для отслеживания и анализа его работы.
#  Логгирование может быть полезно для:
#
#     Отслеживания входящих и исходящих сообщений бота
#     Мониторинга ошибок и исключений, возникающих во время работы бота
#     Анализа производительности бота и оптимизации его работы
#     Отслеживания действий пользователей с ботом
#     Анализа популярности и использования различных функций бота

logging.basicConfig(level=logging.INFO)

#  "parse_mode" в aiogram используется для указания формата сообщения, который будет отправлен пользователю.
bot = Bot(token=config.TOKEN, parse_mode = 'html')
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)