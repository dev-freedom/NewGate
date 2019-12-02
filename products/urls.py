from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductIndex.as_view(), name='list'),
    path('add/', views.ProductCreate.as_view(), name='product-create'),
    path('<slug>/', views.ProductDetail.as_view(), name='product-detail'),
    path('<slug>/update', views.ProductUpdate.as_view(), name='product-update'),
    path('<slug>/delete', views.ProductDelete.as_view(), name='product-delete'),
    path('order', views.OrderView.as_view(), name='order-view'),
    path('order/<slug>', views.add_order, name='add-cart')
]