from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("profile/", views.profile_detail, name="profile"),
]

