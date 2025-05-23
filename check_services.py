import time
import requests
import logging
from collections import defaultdict
from config import urls, time_treshold, error_limit
from notification_bot import send_message
#задаем счетчики
error_count = defaultdict(int) #кол-во ошибок
last_status_code = defaultdict(int) #код ошибки
#проверяем сервис
def check_service(url):
    try:
        start_time = time.time()
        response = requests.post(url, timeout=5) #запрос
        response_time = time.time() - start_time #замерили время
        status_code = response.status_code
        logging.info(f'URL: {url} | Status: {status_code} | Time: {response_time:.2f}s')

        is_unstable = False
        error_message = ''
#если статус не 2хх
        if not (200 <= status_code < 300):
            error_message = f'Status {status_code}'
            is_unstable = True
#если ответ дольше положенного
        if response_time > time_treshold:
            error_message = f'Slow response({response_time:.2f}s'
            is_unstable = True
#если одна ошибка повторяется 3+ раза
        if status_code == last_status_code[url]:
            error_count[url] += 1
            if error_count[url] >= error_limit and status_code >= 400:
                error_message = f'Repeated {status_code} ({error_count[url]} times'
                is_unstable = True
        else:
            error_count[url] = 1 #сбрасываем счетчик если ошибка с другим кодом

        last_status_code[url] = status_code #ластовый статус

        if is_unstable:
            send_message(url, error_message, status_code)#если ничего не работает отправляем сообщение
    except requests.RequestException as e:
        logging.error(f'URL: {url} | Error: {e}')
        send_message(url, f'Request failed: {e}', "N/A")
