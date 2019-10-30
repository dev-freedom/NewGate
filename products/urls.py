from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductIndex.as_view(), name='list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='detail_product'),
    path('create', views.get_product, name='create_product'),
    path('about', views.product_about, name='about'),
    path('contact', views.product_contact, name='contact'),

]