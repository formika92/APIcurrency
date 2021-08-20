from django.urls import (
    path,
)

from rest_framework.routers import SimpleRouter

from currency.views import (
    CurrencyValueViewSet,
)
from currency.viewsets import CurrencyListViewSet

app_name = 'currency'

urlpatterns = [
    path('currency_value', CurrencyValueViewSet.as_view()),
]

router = SimpleRouter()
router.register(r'currency_list', CurrencyListViewSet)

urlpatterns += router.urls
