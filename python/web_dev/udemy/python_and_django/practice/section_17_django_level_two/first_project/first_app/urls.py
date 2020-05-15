from django.urls import include, path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
]
