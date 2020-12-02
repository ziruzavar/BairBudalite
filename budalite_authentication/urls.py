from django.urls import path

from budalite_authentication.views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile')
]