import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from data.config import TOKEN


@dp.message_handler(commands='start')
async def start(message: types.Message):


"""from data.database import Database"""

#from handlers.admin import admin_handler
#from handlers.user import user_handler

"""from handlers.user import check_user"""

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher instances
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

"""db = Database("database.db")
db.create_table()"""




# Register message handlers admin/user
#dp.register_message_handler(admin_handler)
#dp.register_message_handler(user_handler)

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
