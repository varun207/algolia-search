from django.urls import path, include
from .views import productList, productAdd, productSearch, productDetail

urlpatterns = [
    path('', productList, name='product-list'),
    path('add/', productAdd, name='product-add'),
    path('search/', productSearch, name='product-search'),
    path('product/<int:id>', productDetail, name='product-detail')
    # path('runseeder/', fetch_data_from_database, name='upload-data'),
]
