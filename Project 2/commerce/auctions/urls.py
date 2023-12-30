from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("filterCategory", views.filterCategory, name="filterCategory"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removeWatchlist/<int:id>", views.removeWatchlist, name="removeWatchlist"),
    path("addWatchlist/<int:id>", views.addWatchlist, name="addWatchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("addBid/<int:id>", views.addBid, name="addBid"),
    path("closeAuction/<int:id>", views.closeAuction, name="closeAuction"),
]
