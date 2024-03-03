
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("timeline_fetch/", views.timeline_fetch, name="timeline_fetch"),
    path("timeline_post/", views.timeline_post, name="timeline_post"),
    path("timeline_edit/<int:timeline_id>", views.timeline_edit, name="timeline_edit"),
    path("timeline_delete/<str:timeline_subject>/", views.timeline_delete, name="timeline_delete"),
    path("referral/", views.referral, name="referral"),
    path("referral_fetch/", views.referral_fetch, name="referral_fetch"),
    path("referral_delete/<str:referral_subject>/", views.referral_delete, name="referral_delete"),
    path("contact/", views.contact, name="contact"),
    path("contact_fetch/", views.contact_fetch, name="contact_fetch"),
    path("contact_read/<int:contact_id>/", views.contact_read, name="contact_read"),
]
