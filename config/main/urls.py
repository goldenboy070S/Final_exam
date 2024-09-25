from django.urls import path
from .views import *

urlpatterns = [
    path('', CarAPIView.as_view(), name='Api'),
    path('<int:pk>/', CarAPIdetail.as_view(), name='Api_detail'),
    path('api/car/<int:pk>/', CarAPI.as_view(), name='car'),
    path('api/news/<int:pk>/', NewsAPI.as_view(), name='mews'),
    path('api/pro/<int:pk>/', ProductAPI.as_view(), name='products'),
    path('api/book/', BookAPI.as_view(), name='book'),
    path('api/book/<int:pk>/', BookAPI.as_view()),
    path('api/move/', MoviewApi.as_view(), name='move'),
    path('api/move/<int:pk>/', MoviewApi.as_view()),
    path('api/comment/', CommentAPI.as_view(), name='comment'),
    path('api/comment/<int:pk>/', CommentAPI.as_view()),
    path('api/category/', CategoryAPI.as_view(), name='category'),
    path('api/category/<int:pk>/', CategoryAPI.as_view()),

]