from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView
from .forms import SignUpForm


def userView(request):
    qs = User.objects.all()
    return render(request, 'base.html', {'allusers': qs})

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')






# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')



