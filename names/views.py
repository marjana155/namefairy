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
    letter = request.GET["letter"]
    cat = get_object_or_404(Category, title=category)
    gen = get_object_or_404(Gender, title=gender)
    names = Name.objects.filter(category=cat, gender=gen)
    namelist = []
    for name in names:
        if letter != '':
            if name.name[0] == letter.upper():
                namelist.append(name.name)
        else:
            namelist.append(name.name)
    if namelist != []:
        name = random.choice(namelist)
    else:
        name = "Sorry!! we don't have any name with your given criteria yet"

    return render(request, 'action.html', {'name': name})
