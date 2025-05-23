import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
#pip install dotenv
load_dotenv()

#юрл сервисов
urls = ['http://formit.fake', 'http://datavalidator.fake', 'http://leadsync.fake', 'http://bitdashboard.fake']

#берем из файла .env токены для бота и админа, который будет получать сообщения с логами ошибок
bot = Bot(token=os.getenv('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
admin = os.getenv('ADMIN_CHAT_ID')
dp = Dispatcher()

#задаем дефолт времени отклика и лимит ошибок
time_treshold = 2
error_limit = 3

#задаем файл для записи логов ошибок и тд.
log_file = 'monitoring.log'