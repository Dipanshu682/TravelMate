from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import TripPreferenceForm, CommentForm
from .models import TripPreference, Comment


@login_required
def create_trip_preference(request):
    if request.method == "POST":
        form = TripPreferenceForm(request.POST)
        if form.is_valid():
            trip_preference = form.save(commit=False)
            trip_preference.user = request.user
            trip_preference.save()
            return redirect("trip_preference")
    else:
        form = TripPreferenceForm()
    return render(request, "trips/create_trip_preference.html", {"form": form})


@login_required
def trip_preference(request):
    trip_preferences = TripPreference.objects.filter(user=request.user)
    return render(
        request, "trips/trip_preference.html", {"trip_preferences": trip_preferences}
    )


@login_required
def edit_trip_preference(request, pk):
    trip_preference = get_object_or_404(TripPreference, pk=pk, user=request.user)
    if request.method == "POST":
        form = TripPreferenceForm(request.POST, instance=trip_preference)
        if form.is_valid():
            form.save()
            return redirect("trip_preference")
    else:
        form = TripPreferenceForm(instance=trip_preference)
    return render(request, "trips/edit_trip_preference.html", {"form": form})


@login_required(login_url="users/login")
def home(request):
    current_user = request.user

    user_trip_preferences = TripPreference.objects.filter(user=current_user)

    if user_trip_preferences.exists():
        destination = user_trip_preferences.first().destination

        trip_preferences = (
            TripPreference.objects.filter(destination__iexact=destination)
            .exclude(user=current_user)
            .order_by("date")
        )
    else:
        trip_preferences = []

    return render(request, "trips/home.html", {"trip_preferences": trip_preferences})


@login_required(login_url="users/login")
def explore(request):
    trip_preferences = TripPreference.objects.all().order_by("-date")
    return render(request, "trips/explore.html", {"trip_preferences": trip_preferences})


@login_required
def add_comment(request, pk):
    trip = get_object_or_404(TripPreference, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.trip = trip
            comment.user = request.user
            comment.save()
            return redirect("home")
    else:
        form = CommentForm()
    return render(request, "trips/add_comment.html", {"form": form, "trip": trip})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")
    comment.delete()
    return redirect("home", pk=comment.trip.id)
