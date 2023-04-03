from django.urls import path
from .views import projects ,project

urlpatterns = [ 
    path('' , projects , name='projects') , 
    path('project/<str:pk>/' , project , name='project') , 
]