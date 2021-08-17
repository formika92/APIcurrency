from datetime import (
    datetime,
)


def parse_datetime(date):
    """
    Преобразует строковое представление даты в формате YYYY-MM-DD
    в формат DD/MM/YYYY
    """
    errors_list = []
    date_object = None
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
        date_object = datetime.strftime(date_object, '%d/%m/%Y')
    except ValueError:
        errors_list.append(f'Неверный формат даты {date}.')

    return date_object, errors_list


