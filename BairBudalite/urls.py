from django.urls import path

from BairBudalite.views import elements, pohod, IndexView, PohodiView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pohodi', PohodiView.as_view(), name='pohodi'),
    path('elements', elements),
    path('pohod/<int:pk>', pohod,name='pohod'),
    #path('gallery', gallery),

]