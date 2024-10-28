from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe

def recipes(request):
    if request.method == 'POST':
        # check if post and store the data
        data = request.POST
        # parse the data
        recipe_img = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        
        Recipe.objects.create(
            recipe_img = recipe_img,
            recipe_name = recipe_name,
            recipe_description = recipe_desc,
        )
        return redirect('/')
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            recipe_name__icontains = request.GET.get('search')
        )
    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)

