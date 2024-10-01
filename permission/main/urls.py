from django.urls import path
from .views import *

urlpatterns = [
    path('car/', CarApiview.as_view(), name='car'),
    path('car/<int:pk>/', CarDetailApiview.as_view(), name='car-detail'),
    path('brand/', BrandApiview.as_view(), name='brand'),
    path('brand/<int:pk>/', BrandDetailApiview.as_view(), name='brand-detail'),
    path('color/', ColorApiview.as_view(), name='color'),
    path('color/<int:pk>/', ColorDetailApiview.as_view(), name='color-detail'),
    
]
