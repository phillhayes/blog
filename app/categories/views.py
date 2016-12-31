from django.shortcuts import render
from django.http import HttpResponse

from .models import Category
# Create your views here.
def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/show-all.html', {'categories': categories})