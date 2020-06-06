from django.shortcuts import render
from recipes.models import Recipe, Ingredient
from .forms import recipeForm

def recipe_index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_index.html', context)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    context = {
        "recipe": recipe,
        "ingredients": ingredients
    }
    return render(request, 'recipe_detail.html', context)

def recipe_entry(request):
    form = recipeForm(request.POST)
    context = {
        "form": form,
    }
    if request.method == 'POST':
        if form.is_valid():
            print(form)
        else:
            pass
    else:
        return render(request, 'recipe_entry.html', context)
