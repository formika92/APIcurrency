from django.urls import (
    path,
)

from currency.views import (
    CurrencyValueViewSet,
    CurrencyListViewSet,
)

app_name = 'currency'

urlpatterns = [
    path('currency_list', CurrencyListViewSet.as_view()),
    path('currency_value', CurrencyValueViewSet.as_view()),
]
