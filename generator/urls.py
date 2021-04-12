from django.urls import path

from generator import views


app_name = 'generator'

urlpatterns = [
    path('', views.home, name='home'),
    path('mot-de-passe', views.password, name='password'),
]
