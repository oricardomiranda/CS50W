
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("edit/<int:timeline_id>", views.edit, name="edit"),
    path("timeline_fetch/", views.timeline_fetch, name="timeline_fetch"),
    path("timeline_post/", views.timeline_post, name="timeline_post"),
    path("referral/", views.referral, name="referral"),
    path("referral_fetch/", views.referral_fetch, name="referral_fetch"),
    path("contact/", views.contact, name="contact"),
    path("contact_fetch/", views.contact_fetch, name="contact_fetch"),
    # path("career/", views.career, name="career")
]
