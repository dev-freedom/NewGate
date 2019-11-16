from django.urls import path
from orders.views import OrderDetail
urlpatterns = [
    path('', OrderDetail.as_view(), name='order-detail')
]