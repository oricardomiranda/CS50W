from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import json

from .models import User, Post, Career, Referral


def career(request):
    return

def edit(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_post = Post.objects.get(pk=post_id)
        edit_post.message = data["message"]
        edit_post.save()

        return JsonResponse({"message": "Change successful", "New message": data["message"]})


def index(request):
    all_posts = Post.objects.all().order_by("id").reverse()

    # Add paginator
    paginator = Paginator(all_posts, 10)

    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)



    return render(request, "capstone/index.html", {
        "all_posts": all_posts,
        "page_posts": page_posts,
        "user": request.user,
    })


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user_posts = Post.objects.filter(user=user).order_by("id").reverse()

    # Follower counter
    following = Follower.objects.filter(user=user)
    followers = Follower.objects.filter(follower=user)

    # Follow button
    try:
        check_follow = followers.filter(user=User.objects.get(pk=request.user.id))
        if len(check_follow) != 0:
            is_following = True
        else:
            is_following = False
    except:
        is_following = False

    # Paginator
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    return render(request, "capstone/profile.html", {
        "username": user.username,
        "user_posts": user_posts,
        "page_posts": page_posts,
        "following": following,
        "followers": followers,
        "is_following": is_following,
        "user_profile": user

    })


def following(request):
    user = User.objects.get(pk=request.user.id)
    following_people = Follower.objects.filter(user=user)
    all_posts = Post.objects.all().order_by("id").reverse()

    following_posts = []

    for post in all_posts:
        for person in following_people:
            if person.follower == post.user:
                following_posts.append(post)

    # Add paginator
    paginator = Paginator(following_posts, 10)

    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    return render(request, "capstone/following.html", {
        "page_posts": page_posts,
        "user": request.user
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")


@login_required
def new_post(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        message = request.POST["message"]

        if not message:
            messages.error(request, "Post message cannot be empty.")
            return HttpResponseRedirect(reverse("index"))

        post = Post(user=user, message=message)
        post.save()
        return HttpResponseRedirect(reverse("index"))

def career(request):
    return render(request, "capstone/career.html")
