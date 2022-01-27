from django.shortcuts import render
from django.contrib.auth.models import User

def show_user(request):
    qs = User.objects.all()
    return render(request, 'account/base.html', {'allusers': qs})





