from django.urls import path
from . import views
from .views import hello_world

urlpatterns = [
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('hello/', hello_world, name='hello-world')
]