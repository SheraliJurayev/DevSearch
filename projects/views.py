from django.shortcuts import render
from django.http import HttpResponse

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

def projects_view(request):
    msg = "Helloooooooooooo , you are on the project page."
    context = {
        "message": msg , 
        'projects': projectlist,
    }
    
    return render(request, 'projects/project.html' ,context)

def project_view(request , pk):

    projectObj = None
    for i in projectlist:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html' , {'project':projectObj} )
