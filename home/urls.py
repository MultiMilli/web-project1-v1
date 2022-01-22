from django.urls import path, include
from .views import index, list

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('list/', list, name='list'),
]
