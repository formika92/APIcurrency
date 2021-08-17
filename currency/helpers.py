from datetime import (
    datetime,
)


def parse_datetime(date):
    """

    :param date:
    :return:
    """
    errors_list = []
    date_object = None
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
        date_object = datetime.strftime(date_object, '%d/%m/%Y')
    except ValueError:
        errors_list.append('Неверный формат даты.')

    return date_object, errors_list


