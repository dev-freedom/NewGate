from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductIndex.as_view(), name='list'),
    path('products', views.ProductCategoriesView.as_view(), name='product'),
    path('add/', views.ProductCreate.as_view(template_name='products/create.html'), name='product-create'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('<int:pk>/update', views.ProductUpdate.as_view(), name='product-update'),
    path('<int:pk>/delete', views.ProductDelete.as_view(), name='product-delete')

]