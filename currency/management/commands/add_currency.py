from django.core.management.base import (
    BaseCommand,
)
from django.db import (
    transaction,
)

from currency.models import (
    CurrencyList,
)
from currency.parcers import (
    ParcerAvailableCurrency,
)


class Command(BaseCommand):
    help = 'Add currency list'

    @transaction.atomic(savepoint=False)
    def handle(self, *args, **kwargs):
        CurrencyList.objects.all().delete()
        currency_list = ParcerAvailableCurrency().find_currency_list()

        for index in range(0, len(currency_list), 2):
            currency = CurrencyList()
            currency.name = currency_list[index]
            currency.code = currency_list[index+1]
            currency.save()

        self.stdout.write(f'Successfully loaded {currency_list}')
