from django.urls import (
    path,
    include,
)

app_name = 'currency'

urlpatterns = [
    path('v1/', include('currency.v1urls', namespace='v1')),
]
