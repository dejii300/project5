from django.urls import re_path, include, path
from users.views import dashboard
from . import views
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutuser, name="logout")
]