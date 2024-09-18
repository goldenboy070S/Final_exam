from django.urls import path
from .views import *

urlpatterns = [
    path('', CarAPIView.as_view(), name='Api'),
    path('<int:pk>/', CarAPIdetail.as_view(), name='Api_detail'),
]