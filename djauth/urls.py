from authentication.views import LandingPageView, SignupView, UserDeleteView, UserPassword, UserUpdateView
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LandingPageView.as_view(), name="landing-page"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("<int:pk>/password/", UserPassword.as_view(), name="user-password"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)