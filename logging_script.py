import logging
from datetime import datetime
from config import log_file

#функция логирования, задаем настройки в какой файл записываем, что записываем и какой формат времени будет у записи
def logger():
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')