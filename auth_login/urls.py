from auth_login import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('forgot/', views.forgot),

]
