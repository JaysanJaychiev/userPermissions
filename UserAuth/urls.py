from django.contrib import admin
from django.urls import path, include
from SimpleUser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.userView, name="user_list"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/signups/', views.SignUpView.as_view(), name='signups'),
]
