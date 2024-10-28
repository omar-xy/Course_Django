from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Receipe

def receipes(request):
    if request.method == 'POST':
        # check if post and store the data
        data = request.POST
        # parse the data
        recipe_img = request.FILES.get('receipe_image')
        recipe_name = data.get('receipe_name')
        recipe_desc = data.get('receipe_description')
        Receipe.objects.create(
            receipe_img = recipe_img,
            receipe_name = recipe_name,
            receipe_description = recipe_desc,
        )
        return redirect('/')
    
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            receipe_name__icontains = request.GET.get('search')
        )
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')

    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)
