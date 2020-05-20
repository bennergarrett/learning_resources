from django.urls import include, path
from AppTwo import views

urlpatterns = [
    path('help', views.help, name='help'),
    path('users', views.users, name='users'),
    path('index', views.users, name='index'),
    
]