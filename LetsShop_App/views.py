from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.
def Home(request):
    slides= Slider.objects.all()


    return render(request,'Home.html',{'slides':slides})

def Product_search_view(request):
    form = ProductSearchForm(request.GET)
    Products = Product.objects.all()
    if form.is_valid():
      query = form.cleaned_data.get('query')
      category = form.cleaned_data.get('query')
      sub_category = form.cleaned_data.get('query')
      color = form.cleaned_data.get('query')
      size = form.cleaned_data.get('query')
      condition = form.cleaned_data.get('query')
      if query:
          product=Products.objeccts.filter(Q(title__icontains=query))
      if category:
          product=Products.filter(category=category)
      if sub_category:
          product = Products.filter(sub_category=sub_category)
      if color:
          product = Products.filter(color=color)
      if size:
          product = Products.filter(size=size)
      if condition:
          product = Products.filter(condition=condition)
    Context = {
        'form': form,
        'prod': Products

    }
    return render(request,'Product/search.html',Context)

def super_sub_prod(request, id):
    prod = Product.objects.filter(super_sub_category=id)
    print(prod)
    return render(request, 'Product/super_sub_prod.html')