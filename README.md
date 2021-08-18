API для получения списка доступных валют, значений курса валют на указанные даты и разницы между ними.

Функционал для пользователей системы:

- получение списка доступных валют: GET /api/v1/currency_list
- получение значений курса валют на указанные даты и разницы между ними: GET /api/v1/currency_value?date1=YYYY-MM-DD&date2=YYYY-MM-DD&code=CODE


В параметрах date1, date2 передаются даты в формате YYYY-MM-DD, в параметре code - буквенный код валюты. Пример:
- curl -X GET http://localhost:8000/api/v1/currency_list
- curl -X GET 'http://localhost:8000/api/v1/currency_value?date1=2021-07-13&date2=2006-04-02&code=EUR'

Технологии:
- Django==2.2.10, Django REST framework - для обработки запроса и передачи данных клиенту.
- BeautifulSoup=4.9.3, lxml - для парсинга данных с сайта cbr.ru

Запуск локально:
- virtualenv --python=python3.8 venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py runserver <port>
