from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q

from .models import User, AuctionListing, Category, Comment, Bid


def index(request):
    activeListings = AuctionListing.objects.filter(
        ~Q(isActive=False) | Q(closingDate__lte=timezone.now())
    )
    all_categories = Category.objects.all()
    return render(
        request,
        "auctions/index.html",
        {"listings": activeListings, "categories": all_categories},
    )


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
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


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
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        return render(request, "auctions/create.html", {"categories": all_categories})
    else:
        print(request.POST)

        title = request.POST["title"]
        description = request.POST["description"]
        imageurl = request.POST["imageurl"]
        price = request.POST["price"]
        category = request.POST["category"]
        currentUser = request.user

        category_data = Category.objects.get(category_name=category)
        bid = Bid(bid=float(price), user=currentUser)
        bid.save()

        listing = AuctionListing(
            title=title,
            description=description,
            imageurl=imageurl,
            price=bid,
            category=category_data,
            owner=currentUser,
        )

        listing.save()

        return HttpResponseRedirect(reverse("index"))


@login_required
def addBid(request, id):
    newBid = request.POST["newBid"]
    listingDetails = AuctionListing.objects.get(pk=id)
    isOwner = request.user.username == listingDetails.owner.username
    isListingInWatchlist = request.user in listingDetails.watchlist.all()
    allComments = Comment.objects.filter(listing=listingDetails)
    if int(newBid) > listingDetails.price.bid:
        updateBid = Bid(user=request.user, bid=int(newBid))
        updateBid.save()
        listingDetails.price = updateBid
        listingDetails.bidCount += 1
        listingDetails.save()
        return render(
            request,
            "auctions/listing.html",
            {
                "listing": listingDetails,
                "message": "Successful Bid",
                "update": True,
                "isListingInWatchlist": isListingInWatchlist,
                "isOwner": isOwner,
                "allComments": allComments,
            },
        )
    else:
        return render(
            request,
            "auctions/listing.html",
            {
                "listing": listingDetails,
                "message": "Failed Bid",
                "update": False,
                "isListingInWatchlist": isListingInWatchlist,
                "isOwner": isOwner,
                "allComments": allComments,
            },
        )


def filterCategory(request):
    if request.method == "POST":
        filteredCategory = request.POST["category"]
        category = Category.objects.get(category_name=filteredCategory)
        activeListings = AuctionListing.objects.filter(isActive=True, category=category)
        all_categories = Category.objects.all()
        return render(
            request,
            "auctions/index.html",
            {"listings": activeListings, "categories": all_categories},
        )


def listing(request, id):
    listingDetails = AuctionListing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingDetails.watchlist.all()
    allComments = Comment.objects.filter(listing=listingDetails)
    isOwner = request.user.username == listingDetails.owner.username
    return render(
        request,
        "auctions/listing.html",
        {
            "listing": listingDetails,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments,
            "isOwner": isOwner,
        },
    )


@login_required
def closeAuction(request, id):
    listingDetails = AuctionListing.objects.get(pk=id)
    isOwner = request.user.username == listingDetails.owner.username
    isListingInWatchlist = request.user in listingDetails.watchlist.all()
    allComments = Comment.objects.filter(listing=listingDetails)
    listingDetails.isActive = False
    listingDetails.closingDate = timezone.now()
    listingDetails.save()
    return render(
        request,
        "auctions/listing.html",
        {
            "listing": listingDetails,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments,
            "isOwner": isOwner,
            "update": False,
            "message": "Congratulations! The auction is closed.",
        },
    )


@login_required
def watchlist(request):
    user = request.user
    listings = user.auctionWatchlist.all()
    return render(request, "auctions/watchlist.html", {"listings": listings})


@login_required
def removeWatchlist(request, id):
    listingDetails = AuctionListing.objects.get(pk=id)
    user = request.user
    listingDetails.watchlist.remove(user)
    return HttpResponseRedirect(reverse("listing", args=(id,)))


@login_required
def addWatchlist(request, id):
    listingDetails = AuctionListing.objects.get(pk=id)
    user = request.user
    listingDetails.watchlist.add(user)
    return HttpResponseRedirect(reverse("listing", args=(id,)))


@login_required
def comment(request, id):
    listingDetails = AuctionListing.objects.get(pk=id)
    user = request.user
    message = request.POST["comment"]

    newComment = Comment(author=user, listing=listingDetails, message=message)

    newComment.save()

    return HttpResponseRedirect(reverse("listing", args=(id,)))


@login_required
def get_watchlist_count(request):
    user = request.user
    return user.userWatchlist.count()
