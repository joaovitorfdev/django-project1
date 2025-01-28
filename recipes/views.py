from django.shortcuts import render
from django.http import HttpResponse
from  utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'detail_page': False
    })
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': Recipe.objects.get(id=id),
        'detail_page': True
    })
    