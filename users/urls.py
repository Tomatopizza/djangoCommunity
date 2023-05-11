from django.contrib import admin
from django.urls import path
from users import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.UserView.as_view()),

    path('api/token/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('login/', views.UserLogin.as_view()),
    path('logout', views.UserLogout.as_view()),
    path('mock/', views.mockView.as_view(), name='mock_view'),
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='follow_view'),
]
