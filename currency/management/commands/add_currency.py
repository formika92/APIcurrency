from django.core.management.base import (
    BaseCommand,
)

from currency.models import (
    CurrencyList,
)
from currency.parcers import (
    ParcerAvailableCurrency,
)


class Command(BaseCommand):
    help = 'Add currency list'

    def handle(self, *args, **kwargs):
        CurrencyList.objects.all().delete()
        currency_list = ParcerAvailableCurrency().find_currency_list()

        index = 1
        for _ in currency_list:
            currency = CurrencyList()
            try:
                currency.name = currency_list[index-1]
                currency.code = currency_list[index]
                currency.save()
                index +=2
            except IndexError:
                break

        self.stdout.write(f'Successfully loaded {currency_list}')
