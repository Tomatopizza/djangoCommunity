from django.contrib import admin
from django.urls import path
from users import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import ConfirmEmailView
from dj_rest_auth.registration.views import VerifyEmailView
from django.conf.urls import include

urlpatterns = [
    path("signup/", views.UserView.as_view()),
    path(
        "token/obtain/",
        views.CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path('login/', views.UserLogin.as_view()),
    # path('logout', views.UserLogout.as_view()),
    # path('mock/', views.mockView.as_view(), name='mock_view'),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    # 유효한 이메일이 유저에게 전달
    path(
        "users-confirm-email/",
        VerifyEmailView.as_view(),
        name="users_email_verification_sent",
    ),
    # 유저가 클릭한 이메일(=링크) 확인
    path(
        "users-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
        name="users_confirm_email",
    ),
]
