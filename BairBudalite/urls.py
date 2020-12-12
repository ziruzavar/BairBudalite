from django.urls import path

from BairBudalite.views import elements, pohod, IndexView, PohodiView, DeleteCommentView, ProjectsView, ProjectView, \
    ProjectsViewWithPk

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    path('pohodi', PohodiView.as_view(), name='pohodi'),
    path('pohod/<int:pk>', pohod,name='pohod'),
    
    path('projects', ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectsViewWithPk.as_view(), name='projects with pk'),
    path('project/<int:pk>', ProjectView.as_view(), name='project'),
    
    path('elements', elements),
    
    path('delete/comment/<int:pk>', DeleteCommentView.as_view(), name='delete comment'),
    # path('gallery', gallery),
]