from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

from .models import User, Timeline, Contact, Referral

#Referral
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
            'id': referral_obj.id,
            'name': referral_obj.name,
            'subject': referral_obj.subject,
            'message': referral_obj.message
        }
        referral_items.append(referral_item)

    return JsonResponse({'referral_items': referral_items})

@login_required
def referral_delete(request, referral_subject):
    if request.method == "DELETE":
        referral = get_object_or_404(Referral, pk=referral_subject)
        referral.delete()
        return JsonResponse({"message": "Referral event deleted successfully"})
    else:
        return JsonResponse({"error": "Only DELETE requests are allowed"}, status=405)


#Timeline
def timeline_fetch(request):
    timeline_objects = Timeline.objects.all()
    timeline_items = []
    for timeline_obj in timeline_objects:
        timeline_item = {
            'id': timeline_obj.id,
            'year': timeline_obj.year,
            'subject': timeline_obj.subject,
            'content': timeline_obj.content
        }
        timeline_items.append(timeline_item)
    return JsonResponse({'timeline_items': timeline_items})

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

@login_required
def timeline_delete(request, timeline_subject):
    if request.method == "DELETE":
        timeline = get_object_or_404(Timeline, pk=timeline_subject)
        timeline.delete()
        return JsonResponse({"message": "Timeline event deleted successfully"})
    else:
        return JsonResponse({"error": "Only DELETE requests are allowed"}, status=405)

@login_required
def timeline_edit(request, timeline_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        timeline_event = get_object_or_404(Timeline, pk=timeline_id)

        year = data.get("year")
        subject = data.get("subject")
        content = data.get("content")

        if year is not None and subject is not None and content is not None:
            timeline_event.year = year
            timeline_event.subject = subject
            timeline_event.content = content
            timeline_event.save()

            return JsonResponse({"message": "Timeline event updated successfully"})
        else:
            return JsonResponse({"error": "Invalid data provided"}, status=400)
    else:
        return JsonResponse({"error": "Only PUT requests are allowed"}, status=405)



#Contact
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
            'id': contact_obj.id,
            'email': contact_obj.email,
            'phone': contact_obj.phone,
            'message': contact_obj.message,
            'read': contact_obj.read
        }
        contact_items.append(contact_item)

    # Pass the contact items to the template as context
    # return render(request, "capstone/contact.html", {'contact_items': contact_items})
    return JsonResponse({'contact_items': contact_items})

def contact_read(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
        contact.read = True
        contact.save()
        return JsonResponse({'success': True})
    except Contact.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Contact not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


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

#Do not remove
def profile(request, user_id):
    user = User.objects.get(pk=user_id)

    return render(request, "capstone/index.html", {
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
