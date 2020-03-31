from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile', views.profile, name='profile'),
    path('characters', views.characters, name='characters'),
    path('contact', views.contact, name='contact'),
]