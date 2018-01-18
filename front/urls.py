from django.urls import path

from .views import pictures

urlpatterns = [
    path('', pictures.index, name='index')
]
