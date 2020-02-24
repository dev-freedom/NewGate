from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductIndex.as_view(), name='list'),
    path('add/', views.ProductCreate.as_view(), name='product-create'),
    path('<int:pk>/detail', views.ProductDetail.as_view(), name='product-detail'),
    path('<int:pk>/update', views.ProductUpdate.as_view(), name='product-update'),
    path('<int:pk>/delete', views.ProductDelete.as_view(), name='product-delete'),
    path('order', views.OrderView.as_view(), name='order-view'),
    path('order/<pk>', views.add_order, name='add-cart'),
]