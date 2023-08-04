from django.urls import path

from .views import *

urlpatterns = [
  path('login/',LOGIN,name='login'),
  path('registration/',Registration,name='registration'),
  path('logout/',LOGOUT,name='reg')
]