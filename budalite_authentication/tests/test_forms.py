from django.test import TestCase

from budalite_authentication.forms import UserForm


class UserFormTest(TestCase):

    def test_CorrectEmail_shouldReturnCorrectForm(self):
        form = UserForm(data={'username': 'test', 'email': 'ivan.vanir@gmail.com',
                              'password1': 'Aa12Bb34',
                              'password2': 'Aa12Bb34'})
        self.assertTrue(form.is_valid())

    def test_IncorrectEmail_shouldReturnError(self):
        form = UserForm(data={'username': 'test', 'email': 'wrong',
                              'password1': 'Aa12Bb34',
                              'password2': 'Aa12Bb34'})
        self.assertFalse(form.is_valid())
