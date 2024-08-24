from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'), 
    path('getuser/<name>/<id>', views.pathview, name='pathview'), 
]