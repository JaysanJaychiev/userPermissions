from django.contrib import admin
from django.urls import path, include
from SimpleUser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.userView, name="user_list"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.SignUpView.as_view(), name='register'),
]
