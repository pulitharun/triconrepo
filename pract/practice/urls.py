from django.urls import path
from .views import *

urlpatterns = [
    path('users/', userview.as_view(), name='user_list'),
    path('users/<int:id>',userview.as_view(), name='user_detail')
]
