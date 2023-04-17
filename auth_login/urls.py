from django.urls import path
from auth_login import views

urlpatterns = [
    path('login/', views.login),
]
