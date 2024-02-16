from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# 전체 app의 하위 페이지 ex. app/login

app_name = 'app'

urlpatterns = [
    path('', views.startapps, name='startapps'),
    path('login', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
]