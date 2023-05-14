from django.contrib import admin
from django.urls import path
from dj_rest_auth.registration.views import VerifyEmailView
from users import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import ConfirmEmailView

from django.conf.urls import include

urlpatterns = [

    path(
        "api/token/",
        views.CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='follow_view'),
    path("signup/", include("dj_rest_auth.registration.urls")),
    path(
        "users-confirm-email/",
        VerifyEmailView.as_view(),
        name="users_email_verification_sent",
    ),
    path(
        "users-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
        name="users_confirm_email",
    ),
]

