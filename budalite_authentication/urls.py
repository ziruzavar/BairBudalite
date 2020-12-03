from django.urls import path

from budalite_authentication.views import RegisterView, LoginView, ProfileView, EditProfileView, LogoutView, \
    DeleteUserView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout view'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', EditProfileView.as_view(), name='edit profile'),
    path('profile/<int:pk>/delete', DeleteUserView.as_view(), name='delete user')
]