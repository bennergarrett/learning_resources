from django.urls import include, path
from AppTwo import views

urlpatterns = [
    path('help', views.help, name='help'),
    
]