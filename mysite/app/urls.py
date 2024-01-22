from django.urls import path
from . import views

# 전체 app의 하위 페이지 ex. app/login

app_name = 'app'

urlpatterns = [
    path('', views.startapps, name='startapps'),
    path('login', views.loginapp, name='login'),
]