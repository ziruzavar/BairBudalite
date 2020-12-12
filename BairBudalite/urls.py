from django.urls import path

from BairBudalite.views import elements, pohod, IndexView, PohodiView, DeleteCommentView, ProjectsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pohodi', PohodiView.as_view(), name='pohodi'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('elements', elements),
    path('pohod/<int:pk>', pohod,name='pohod'),
    path('delete/comment/<int:pk>', DeleteCommentView.as_view(), name='delete comment'),
    # path('gallery', gallery),
]