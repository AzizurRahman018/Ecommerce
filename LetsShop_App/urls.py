
from django.urls import path
from .views import *

urlpatterns = [
  path('',Home,name='home'),
  path('search',Product_search_view,name='Product_search_view'),
  path('super_sub_prod/<int:id>/', super_sub_prod, name='super_sub_prod'),

]