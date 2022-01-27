from django.contrib.auth import get_user_model
from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

    # class Meta:
    #      model = get_user_model()
    #      fields = ("first_name", "last_name", 'email', "username", "password1", "password2")


