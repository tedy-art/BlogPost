from django.urls import path
from users import views as views

urlpatterns = [
    path('users/signup', views.signup, name="signup")
]