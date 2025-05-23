from datetime import datetime
from config import bot, admin

#через аиограм отправляем сообщение админу с содержанием сервиса ошибки и кода ошибки
async def send_message(service: str, error: str, status_code: str):
    message = ('Error in service!\n\n'
               f'Service: {service}\n'
               f'Error: {error}\n'
               f'Code: {status_code}\n'
               f'Time: {datetime.now().strftime('%H:%M:%S')}')
    #если не получилось отправить сообщение, отправляем соответствующее
    try:
        await bot.send_message(chat_id=admin, text=message)
    except Exception as e:
        print(f'send message error: {e}')