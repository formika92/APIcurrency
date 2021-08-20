from django.db import models


class CurrencyList(models.Model):
    name = models.CharField(
        'Наименование валюты',
        max_length=100,
        null=False,
        blank=False,
    )

    code = models.CharField(
        'Код валюты',
        max_length=10,
        null=True,
        blank=True,
    )

    date_modified = models.DateTimeField(
        verbose_name='Дата модификации',
        auto_now=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Список валюты'

    def __str__(self):
        return self.name
