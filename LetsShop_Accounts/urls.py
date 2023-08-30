from django.urls import path

from .views import *

urlpatterns = [
  path('login/',LOGIN,name='login'),
  path('registration/',Registration,name='registration'),
  path('logout/',LOGOUT,name='logout'),
  path('reset/',RESET_PASS,name='reset'),
  path('success/',success,name='success'),
  path('token_send/',token_send,name='token_send'),
  path('error/',error,name='error'),
  path('user_desh/',user_desh,name='user_desh')
]