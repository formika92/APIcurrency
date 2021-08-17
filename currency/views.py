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
    ParcerAvailableCurrency,
    ParcerValueCurrency,
)


class CurrencyListViewSet(APIView):
    def get(self, request):
        """

        :param request:
        :return:
        """
        parser = ParcerAvailableCurrency()
        return Response({'currency_list': f'{parser._find_currency_list()}'})


class CurrencyValueViewSet(APIView):
    def get(self, request):
        """

        :param request:
        :return:
        """
        date_first, errors_list = parse_datetime(
            date=self.request.query_params.get('date1', None),
        )
        date_second, errors_list = parse_datetime(
            date=self.request.query_params.get('date2', None),
        )

        if date_first and date_second:
            code = self.request.query_params.get('code', None)

            result = self.calc_diff_numbers(
                date_first=date_first,
                date_second=date_second,
                code=code,
            )

            result = Response(
                {
                    'difference': f'{result}'
                }
            )
        else:
            result = Response({'Error': f'{errors_list}'})

        return result

    @staticmethod
    def calc_diff_numbers(date_first, date_second, code):
        """

        :param date_first:
        :param date_second:
        :param code:
        :return:
        """
        num_first = ParcerValueCurrency(
            date=date_first,
        )._find_value_currency(
            code=code,
        )
        num_second = ParcerValueCurrency(
            date=date_second,
        )._find_value_currency(
            code=code,
        )

        return num_first - num_second

