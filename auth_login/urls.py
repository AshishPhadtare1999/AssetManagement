from django.urls import path
from auth_login import views

urlpatterns = [
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]
