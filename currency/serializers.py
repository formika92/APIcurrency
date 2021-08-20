from rest_framework import serializers


class CurrencyListSerializer(serializers.Serializer):
    """
    """
    name = serializers.CharField(
        max_length=100,
    )
    code = serializers.CharField(
        max_length=10,
    )
