from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from currency.helpers import (
    parse_datetime,
)
from currency.parcers import (
    ParcerValueCurrency,
)


class CurrencyValueViewSet(APIView):

    def get(self, request):
        date_first, errors_first = parse_datetime(
            date=self.request.query_params.get('date1'),
        )
        date_second, errors_second = parse_datetime(
            date=self.request.query_params.get('date2'),
        )

        if date_first and date_second:
            code = self.request.query_params.get('code')

            result = Response(
                self.calc_diff_numbers(
                    date_first=date_first,
                    date_second=date_second,
                    code=code,
                )
            )
        else:
            result = Response({'Error': f'{errors_first + errors_second}'})

        return result

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
