from django.urls import path
from .views import *

urlpatterns = [
    path('', CarAPIView.as_view(), name='Api'),
    path('<int:pk>/', CarAPIdetail.as_view(), name='Api_detail'),
    path('api/car/', CarAPI.as_view(), name='car'),
    path('api/news/', NewsAPI.as_view(), name='mews'),
    path('api/pro/', ProductAPI.as_view(), name='products')
]