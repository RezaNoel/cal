from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
import os
from .models import Project, Sprint, Task
from .forms import ProjectForm, SprintForm, TaskForm
from django.contrib.auth.decorators import login_required




def home(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('project_list_view')  # Redirect to dashboard or any other page
    else:
        form = CustomAuthenticationForm()

    cms_name = os.getenv('CMS_NAME')
    return render(request, 'cms/home.html', {'form': form,'cms_name':cms_name})

def panel(request):
    return render(request, 'cms/panel.html')

@login_required
def project_list_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'cms/project_list.html', context)

def sprint_list_view(request, project_id):
    project = Project.objects.get(id=project_id)
    sprints = Sprint.objects.all()
    context = {
        'project': project,
        'sprints': sprints,
    }
    return render(request, 'cms/sprint_list.html', context)

def task_list_view(request,project_id, sprint_id):
    project = Project.objects.get(id=project_id)
    sprint = Sprint.objects.get(id=sprint_id)
    tasks = Task.objects.all()
    context = {
        'project': project,
        'sprint': sprint,
        'tasks': tasks,
    }
    return render(request, 'cms/task_list.html', context)

def project_detail_view(request, project_id):
    project = Project.objects.get(id=project_id)
    sprints = Sprint.objects.filter(project=project)
    context = {
        'project': project,
        'sprints': sprints
    }
    return render(request, 'cms/project_detail.html', context)

def sprint_detail_view(request, project_id, sprint_id):
    project = Project.objects.get(id=project_id)
    sprint = Sprint.objects.get(id=sprint_id)
    tasks = Task.objects.filter(sprint=sprint)
    context = {
        'project': project,
        'sprint': sprint,
        'tasks': tasks,
    }
    return render(request, 'cms/sprint_detail.html', context)

def task_detail_view(request, project_id, sprint_id, task_id):
    project = Project.objects.get(id=project_id)
    sprint = Sprint.objects.get(id=sprint_id)
    task = Task.objects.get(sprint=sprint)
    context = {
        'project': project,
        'sprint': sprint,
        'task': task,
    }
    return render(request, 'cms/task_detail.html', context)

def create_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list_view')
    else:
        form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request, 'cms/project_create.html', context)


def create_sprint_view(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = SprintForm(request.POST)
        if form.is_valid():
            sprint

# ... ویوهای لیست (project_list_view, sprint_list_view, task_list_view) مشابه قبل ...

@login_required
def create_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list_view')
    else:
        form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request, 'cms/project_create.html', context)

@login_required
def create_sprint_view(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = SprintForm(request.POST)
        if form.is_valid():
            sprint = form.save(commit=False)
            sprint.project = project
            sprint.save()
            return redirect('project_detail_view', project_id)
    else:
        form = SprintForm()
    context = {
        'form': form,
        'project': project,
    }
    return render(request, 'cms/sprint_create.html', context)

@login_required
def create_task_view(request, project_id, sprint_id):
    project = Project.objects.get(id=project_id)
    sprint = Sprint.objects.get(id=sprint_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.sprint = sprint
            task.save()
            return redirect('sprint_detail_view', project_id, sprint_id)
    else:
        form = TaskForm()
    context = {
        'form': form,
        'project': project,
        'sprint': sprint,
    }
    return render(request, 'cms/task_create.html', context)

@login_required
def edit_project_view(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list_view')
    else:
        form = ProjectForm(instance=project)
    context = {
        'form': form,
        'project': project,
    }
    return render(request, 'cms/project_edit.html', context)

@login_required
def edit_sprint_view(request, project_id, sprint_id):
    project = Project.objects.get(id=project_id)
    sprint = project.sprints.get(id=sprint_id)
    if request.method == 'POST':
        form = SprintForm(request.POST, instance=sprint)
        if form.is_valid():
            form.save()
            return redirect('project_detail_view', project_id)
    else:
        form = SprintForm(instance=sprint)
    context = {
        'form': form,
        'project': project,
        'sprint': sprint,
    }
    return render(request, 'cms/sprint_edit.html', context)

@login_required
def edit_task_view(request, project_id, sprint_id, task_id):
    project = Project.objects.get(id=project_id)
    sprint = Sprint.objects.get(id=sprint_id)
    task = Task.objects.get(sprint=sprint)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('sprint_detail_view', project_id, sprint_id)
    else:
        form = TaskForm(instance=task)
    context = {
        'form': form,
        'project': project,
        'sprint': sprint,
        'task': task,
    }
    return render(request, 'cms/task_edit.html', context)

@login_required
def delete_project_view(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect('project_list_view')


@login_required
def delete_sprint_view(request, project_id, sprint_id):
    project = Project.objects.get(id=project_id)
    sprint = project.sprints.get(id=sprint_id)
    sprint.delete()
    return redirect('project_detail_view', project_id)



@login_required
def delete_task_view(request, project_id, sprint_id, task_id):
    project = Project.objects.get(id=project_id)
    sprint = Sprint.objects.get(id=sprint_id)
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('sprint_detail_view', project_id, sprint_id)


