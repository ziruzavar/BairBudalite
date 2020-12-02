from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView

from budalite_authentication.forms import UserForm, UserProfileForm, LoginForm
from budalite_authentication.models import UserProfile


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'form': UserForm,
            'form_profile': UserProfileForm,
        }
        return render(request, 'auth/register.html', context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and form.clean_email() and profile_form.is_valid():
            user = form.save()
            picture = profile_form.cleaned_data['profile_picture']
            user_profile = UserProfile(user_id=user.id, profile_picture=picture)
            user.save()
            user_profile.save()
            return redirect('index')
        else:
            context = {
                'form': UserForm,
                'form_profile': UserProfileForm,
            }
            return render(request, 'auth/register.html', context)


class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form_cleaned = form.cleaned_data
        user = authenticate(username=form_cleaned['username'], password=form_cleaned['password'])
        if user:
            login(self.request, user)
            return redirect('index')
        return super().form_valid(form)


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user_id=kwargs['pk'])
        context = {
            'user_profile': user_profile,
        }
        return render(request, 'auth/profile.html', context)
