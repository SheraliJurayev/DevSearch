from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {
        "form" : form
        }
    return render(request, 'projects/project-form.html' , context)

@login_required(login_url='login')
def updateProject(request , pk ):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST , request.FILES , instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form" : form
        }
    return render(request, 'projects/project-form.html' , context)

@login_required(login_url='login')
def deleteProject(request , pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request , 'delete_template.html', context)