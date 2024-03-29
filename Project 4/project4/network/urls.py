
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
	path("new_post/", views.new_post, name="new_post"),
	path("follow", views.follow, name="follow"),
	path("unfollow", views.unfollow, name="unfollow"),
	path("following/", views.following, name="following"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("remove_like/<int:post_id>/", views.remove_like, name="remove_like"),
    path("add_like/<int:post_id>/", views.add_like, name="add_like"),
	path('count_like/<int:post_id>/', views.count_like, name='count_like')
]
