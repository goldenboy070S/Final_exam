from django.urls import path
from .views import *

urlpatterns = [
    path('', CarAPIView.as_view(), name='Api'),
    path('<int:pk>/', CarAPIdetail.as_view(), name='Api_detail'),
    path('api/car/<int:pk>/', CarAPI.as_view()),
    path('api/news/', NewsAPI.as_view(), name='mews'),
    path('api/pro/', ProductAPI.as_view(), name='products'),
    path('api/news/<int:pk>/', NewsAPI.as_view(), name='mews'),
    path('api/pro/<int:pk>/', ProductAPI.as_view(), name='products')
]