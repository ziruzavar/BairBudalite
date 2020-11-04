from django.urls import path

from BairBudalite.views import index, pohodi, elements, pohod

urlpatterns = [
    path('', index, name='index'),
    path('pohodi', pohodi, name='pohodi'),
    path('elements', elements),
    path('pohod/<int:pk>', pohod,name='pohod'),
]