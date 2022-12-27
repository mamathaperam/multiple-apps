from django.urls import path
from app1.views import *
app_name='ammu'
urlpatterns=[
    path('mamatha/',mamatha,name='mamatha'),
]