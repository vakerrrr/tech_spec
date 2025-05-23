import logging
import time
from logging_script import logger
from check_services import check_service
from config import urls
import schedule
#функция проверки
def check_all_services():
    logging.info('Начинаем проверку...')
    for service in urls:
        check_service(service)
    logging.info('Проверка завершена.\n\n')

def main():
    logger()#логирование
    check_all_services()#проверяем
#ставим таймер на 5 минут
    schedule.every(5).minutes.do(check_all_services)
#цикл на запуск
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
