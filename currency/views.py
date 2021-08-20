from datetime import (
    datetime,
)

from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from currency.parcers import (
    ParcerValueCurrency,
)


class CurrencyValueViewSet(APIView):

    def get(self, request):
        date_first = self.request.query_params.get('date1')
        date_second = self.request.query_params.get('date2')
        code = self.request.query_params.get('code')

        try:
            date_first = datetime.strptime(date_first, '%Y-%m-%d')
            date_first = datetime.strftime(date_first, '%d/%m/%Y')

            date_second = datetime.strptime(date_second, '%Y-%m-%d')
            date_second = datetime.strftime(date_second, '%d/%m/%Y')

        except (ValueError, TypeError):
            return Response({'Error': f'Неверный формат даты'})


        return Response(
            self.calc_diff_numbers(
                date_first=date_first,
                date_second=date_second,
                code=code,
            )
        )

    @staticmethod
    def calc_diff_numbers(date_first, date_second, code):
        """
        Возвращает курсы валют на указанные даты и разницу курсов.
        """

        num_first = ParcerValueCurrency(
            date=date_first,
        ).find_value_currency(
            code=code,
        )
        num_second = ParcerValueCurrency(
            date=date_second,
        ).find_value_currency(
            code=code,
        )

        result = {
            date_first: num_first,
            date_second: num_second,
        }

        if num_first and num_second:
            result['difference'] = num_first - num_second
        else:
            result['Error'] = 'Не найдено значение валюты на указанную дату'

        return result
