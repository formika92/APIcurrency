from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from currency.filters import CurrencyListFilter
from currency.models import CurrencyList
from currency.parcers import ParcerAvailableCurrency
from currency.serializers import CurrencyListSerializer


class CurrencyListViewSet(ListModelMixin, GenericViewSet):
    queryset = CurrencyList.objects.all()
    serializer_class = CurrencyListSerializer
    filterset_class = CurrencyListFilter

    def get(self, request, input_code=None):
        # Извлекаем набор всех записей из таблицы
        if self.filter.exists():
            # Создаём сериалайзер для извлечённого наборa записей
            serializer_for_queryset = CurrencyListSerializer
            return Response(serializer_for_queryset.data)
