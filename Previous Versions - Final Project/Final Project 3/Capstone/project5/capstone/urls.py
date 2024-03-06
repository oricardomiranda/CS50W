
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/login/", views.login_view, name="login"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("edit/<int:timeline_id>", views.edit, name="edit"),
    path("timeline_data/", views.timeline_data, name="timeline_data"),
    # path("career/", views.career, name="career")
]
