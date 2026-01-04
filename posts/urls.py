from django.contrib import admin
from django.urls import path
from posts import views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogposts', views.blogposts, name='blogposts'),
    path('create', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('details/<int:pk>', views.details, name='details')
]
