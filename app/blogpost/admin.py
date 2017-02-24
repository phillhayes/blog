from django.contrib import admin
from .models import Blogpost
from .models import Category

# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Category)
