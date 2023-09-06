from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def Home(request):
    slides= Slider.objects.all()
    Products = Product.objects.all()
    feture_prod = Products.filter(featured_product = True)

    return render(request,'Home.html',{'slides':slides, 'feture_prod':feture_prod })

def Product_search_view(request):
    try:
        form = ProductSearchForm(request.GET)
        Products = Product.objects.all()
        if form.is_valid():
          query = form.cleaned_data.get('query')
          category = form.cleaned_data.get('category')
          sub_category = form.cleaned_data.get('sub_category')
          color = form.cleaned_data.get('color')
          size = form.cleaned_data.get('size')
          condition = form.cleaned_data.get('condition')
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
        # Context = {
        #     'form': form,
        #     'prod': Products
        #
        # }
    except Exception as e:
        messages.warning(request, "No product available")
        return redirect('search')
    return render(request,'Product/search.html',locals())
def super_sub_prod(request, id):
    prod = Product.objects.filter(super_sub_category=id)
    print(prod)
    return render(request, 'Product/super_sub_prod.html')
