from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


def login_view(request):
    if request.method == "POST":
        user = authenticate(request,
                            username=request.POST.get("username"),
                            password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect("pages:home")
        messages.error(request, "Identifiants incorrects.")
    return render(request, "accounts/login.html")


@require_POST
def logout_view(request):
    logout(request)
    return redirect("accounts:login")