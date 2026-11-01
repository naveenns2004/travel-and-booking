from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


def landing(request):
    return render(request, "accounts/landing.html")


def register(request):
    error = ""
    email = ""
    name = ""
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        name = request.POST.get("name", "").strip()

        try:
            validate_email(email)
        except ValidationError:
            error = "Enter a valid email address."

        if not error:
            if not name:
                error = "Enter your name."
            elif len(name) > 150:
                error = "Name must be 150 characters or fewer."
            elif len(email) > 150:
                error = "Email must be 150 characters or fewer."
            elif len(password) < 8:
                error = "Password must contain at least 8 characters."
            elif password != confirm_password:
                error = "Passwords do not match."
            elif User.objects.filter(username=email).exists():
                error = "An account with this email already exists."
            else:
                # Use the email as the username to keep email login simple.
                # create_user securely hashes the password for us.
                # Store the entered name in Django's built-in first_name field.
                User.objects.create_user(
                    username=email, email=email, password=password, first_name=name
                )
                return redirect("login")

    return render(request, "accounts/register.html", {"error": error, "email": email, "name": name})


def login_view(request):
    error = ""
    email = ""
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        error = "Invalid email or password."
    return render(request, "accounts/login.html", {"error": error, "email": email})


@login_required
def home(request):
    return render(request, "accounts/home.html")


@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")
