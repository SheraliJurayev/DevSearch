from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectlist = [
    {
    'id': '1' , 
    'title': 'GitHub Project',
    'description': 'GitHub Project is find our jobs and commands available',
    } , 

    {
    'id': '2' , 
    'title': 'Clone Project',
    'description': 'Clone Project is find our jobs and commands available',
    } ,

    {
    'id': '3' , 
    'title': 'YouTube Project',
    'description': 'YouTube Project is find our jobs and commands available',
    } ,
]

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    
    return render(request, 'projects/project.html' ,context)

def project(request , pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context =  {
        'projectObj':projectObj , 
        'tags':tags 
        }
    return render(request, 'projects/single-project.html' , context )
