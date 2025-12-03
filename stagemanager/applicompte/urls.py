from django.contrib import admin 
from django.urls import path
from applicompte import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'applicompte/login.html'), name = 'login')
]

urlpatterns += static(settings.MEDIA_URL, documant_root = settings.MEDIA_ROOT)