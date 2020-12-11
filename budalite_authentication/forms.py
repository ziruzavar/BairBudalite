from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from budalite_authentication.models import UserProfile


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('You need to enter a valid email!')
        return email


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profile_picture',)


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('description', 'instagram', )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput,
    )