from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Slider)
admin.site.register(Product)
admin.site.register(CONDITION)
admin.site.register(COLOR)
admin.site.register(SIZE)
admin.site.register(SubCategory)
admin.site.register(Category)
