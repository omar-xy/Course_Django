from django.urls import path, re_path
from . import views
app_name = 'demoApp'
urlpatterns =[
    path('', views.index, name='index'), 
    path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name="getform"),
    path('login/', views.login, name='login')
]