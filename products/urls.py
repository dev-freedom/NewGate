from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductIndex.as_view(), name='list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='detail_product'),
    path('create', views.ProductCreate.as_view(), name='create_product'),
    path('about', views.ProductAbout.as_view(), name='about'),
    path('contact', views.ProductContact.as_view(), name='contact'),
]