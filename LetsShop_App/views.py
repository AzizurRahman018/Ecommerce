from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    slides= Slider.objects.all()
    cats = Category.objects.all()


    return render(request,'Home.html',{'slides':slides, 'cats':cats} )