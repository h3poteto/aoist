from django.urls import path

from .views import youtubes

urlpatterns = [
    path('', youtubes.index, name='index')
]
