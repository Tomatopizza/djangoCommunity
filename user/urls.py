from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('signup', views.UserView.as_view()),
    path('login', views.UserLogin.as_view()),
    path('logout', views.UserLogout.as_view()),
]
 