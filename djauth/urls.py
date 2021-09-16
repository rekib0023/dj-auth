from authentication.views import LandingPageView, SignupView, UserDeleteView
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LandingPageView.as_view(), name="landing-page"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
]
