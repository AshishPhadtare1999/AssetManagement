from django.shortcuts import render


def login(request):
    if request.method.lower() == "get":
        return render(request, template_name="login.html")
