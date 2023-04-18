from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method.lower() == "get":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, template_name="login.html")

    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        login(request, user)
        return redirect("/")

    return render(request, template_name="login.html", context={
        "message": "Wrong Credentials!."
    })


@login_required
def logout_user(request):
    logout(request)
    return redirect("/login")
