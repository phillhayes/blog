from django.contrib import admin
from .models import Category, Blogpost

# Register your models here.
admin.site.register(Category)
admin.site.register(Blogpost)