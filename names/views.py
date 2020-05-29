from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Name, Category, Gender
import random
# Create your views here.

c = Category.objects.all()
g = Gender.objects.all


def home(request):

    return render(request, "index.html", {'categories': c, 'genders': g})


def action(request):
    gender = request.GET["gender"]
    category = request.GET["category"]
    cat = get_object_or_404(Category, title=category)
    gen = get_object_or_404(Gender, title=gender)
    names = Name.objects.filter(category=cat, gender=gen)
    namelist = []
    for name in names:
        namelist.append(name.name)
    name = random.choice(namelist)

    return render(request, 'action.html', {'name': name})
