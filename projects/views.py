from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    
    return render(request, 'projects/project.html' ,context)

def project(request , pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context =  {
        'project':project , 
        'tags':tags 
        }
    return render(request, 'projects/single-project.html' , context )

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form" : form
        }
    return render(request, 'projects/project-form.html' , context)


def updateProject(request , pk ):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST , instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form" : form
        }
    return render(request, 'projects/project-form.html' , context)


def deleteProject(request , pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request , 'projects/delete_template.html', context)