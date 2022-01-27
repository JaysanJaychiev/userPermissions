from django.contrib import admin
from django.urls import path, include
from SimpleUser import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_user, name="user_list"),
    path('accounts/', include('allauth.urls')),
]
