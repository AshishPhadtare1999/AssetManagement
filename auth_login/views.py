from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method.lower() == "get":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, template_name="login.html")

    user = authenticate(request, email=request.POST["email"], password=request.POST["password"])
    print(user)
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


def forgot(request):
    if request.method.lower() == "get":
        return render(request, template_name="forgot.html")

    password = request.POST["password"]
    if password != request.POST["c_password"]:
        return render(request, template_name="forgot.html", context={
            "message": "Confirm Password did not match!."
        })
    try:
        user = User.objects.get(email=request.POST["email"])
        user.set_password(password)
        user.save()
        return redirect("/login/")
    except Exception as err:
        return render(request, template_name="forgot.html", context={
            "message": "Email Not Found!."
        })
