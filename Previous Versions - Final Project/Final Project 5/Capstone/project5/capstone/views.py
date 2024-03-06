from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import json

from .models import User, Timeline, Contact, Referral


def referral(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        subject = data.get("subject")
        message = data.get("message")

        if subject and message:
            referral_event = Referral.objects.create(name=name, subject=subject, message=message)
            referral_event.save()

            return JsonResponse({"message": "Referral event created successfully"})
        else:
            return JsonResponse({"error": "Invalid data provided"}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


def referral_fetch(request):
    referral_objects = Referral.objects.all().order_by('name')  # Sort by name
    referral_items = []

    for referral_obj in referral_objects:
        referral_item = {
            'name': referral_obj.name,
            'subject': referral_obj.subject,
            'message': referral_obj.message
        }
        referral_items.append(referral_item)

    return JsonResponse({'referral_items': referral_items})


@login_required
def edit(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_post = Post.objects.get(pk=post_id)
        edit_post.message = data["message"]
        edit_post.save()

        return JsonResponse({"message": "Change successful", "New message": data["message"]})

def timeline_fetch(request):
    timeline_objects = Timeline.objects.all()
    timeline_items = []
    for timeline_obj in timeline_objects:
        timeline_item = {
            'year': timeline_obj.year,
            'subject': timeline_obj.subject,
            'event': timeline_obj.content
        }
        timeline_items.append(timeline_item)
    return JsonResponse({'timeline_items': timeline_items})

##Posting new events with the timeline post button in navbar
@login_required
def timeline_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        year = data.get("year")
        subject = data.get("subject")
        content = data.get("content")

        if year and subject and content:
            timeline_event = Timeline.objects.create(year=year, subject=subject, content=content)
            timeline_event.save()

            return JsonResponse({"message": "Timeline event created successfully"})
        else:
            return JsonResponse({"error": "Invalid data provided"}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        phone = data.get("phone")
        message = data.get("message")

        if email and phone and message:
            new_contact = Contact.objects.create(email=email, phone=phone, message=message)
            new_contact.save()

            return JsonResponse({"message": "Contact form created successfully"})
        else:
            return JsonResponse({"error": "Invalid data provided"}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)

def contact_fetch(request):
    contact_objects = Contact.objects.all()
    contact_items = []
    for contact_obj in contact_objects:
        contact_item = {
            'email': contact_obj.email,
            'phone': contact_obj.phone,
            'message': contact_obj.message
        }
        contact_items.append(contact_item)

    # Pass the contact items to the template as context
    return render(request, "capstone/contact.html", {'contact_items': contact_items})
    #return JsonResponse({'contact_items': contact_items})


def index(request):
    timeline_objects = Timeline.objects.all()

    timeline_items = []
    for timeline_obj in timeline_objects:
        timeline_item = {
            'date': timeline_obj.year,
            'subject': timeline_obj.subject,
            'event': timeline_obj.content
        }
        timeline_items.append(timeline_item)

    return render(request, "capstone/index.html", {
        "user": request.user,
        "timeline_items": timeline_items  # Include timeline items in the context
    })


def profile(request, user_id):
    user = User.objects.get(pk=user_id)


    return render(request, "capstone/profile.html", {
        "username": user.username,
        "user_profile": user

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
