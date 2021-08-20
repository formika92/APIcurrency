import re
import requests

from decimal import (
    Decimal,
)

from bs4 import (
    BeautifulSoup,
)


class ParcerCbr:
    """
    """
    url = 'http://www.cbr.ru/scripts/XML_valFull.asp'
    errors_list = []

    def _get_page(self):
        response = requests.get(self.url)
        if (response.status_code == 200
                and '404' not in response.url):
            return requests.get(self.url)
        else:
            self.errors_list.append(f'Error {requests.get(self.url).status_code}')

    def _get_soup(self):
        page = self._get_page()
        return page if page is None else BeautifulSoup(page.text, 'lxml')


class ParcerAvailableCurrency(ParcerCbr):

    def _get_page(self):
        return super()._get_page()

    def _get_soup(self):
        return super()._get_soup()

    def find_currency_list(self):
        """
        Находит наименования и коды доступных валют
        """
        soup = self._get_soup()
        result_list = []
        if soup:
            # result_list = iter(
            #   re.sub(r'[\[\]]*|\<[^>]*\>', '', str(soup.find_all(['iso_char_code', 'name']))).split(',')
            # )
            # result_list = [curr + next(result_list, '') for curr in result_list]

            result_list = re.sub(
                r'\s*(?=[<])|[\[\]]*|\<[^>]*\>', '', str(soup.find_all(['iso_char_code', 'name']))
            ).split(',')
        else:
            result_list.extend(self.errors_list)

        return result_list


class ParcerValueCurrency(ParcerCbr):

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def __init__(self, date):
        self.url = f'{self.url}?date_req={date}'

    def _get_page(self):
        return super()._get_page()

    def _get_soup(self):
        return super()._get_soup()

    def find_value_currency(self, code):
        soup = self._get_soup()

        for child in soup.valcurs.children:
            if child.findChildren(text=code):
                text = child.value.text
                if text:
                    return Decimal(text.replace(',', '.'))
