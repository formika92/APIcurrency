from django_filters import rest_framework as filters

from currency.models import (
    CurrencyList,
)


class CurrencyListFilter(filters.FilterSet):
    currency_list = filters.CharFilter(method='currency_list')

    class Meta:
        model = CurrencyList
        fields = ('code', 'name')

    def currency_list(self, queryset, code):
        """
        """
        return queryset