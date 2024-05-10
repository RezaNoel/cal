# In your views.py
from django import template
from ..models import Sprint,Task
register = template.Library()

@register.simple_tag
def get_sprint_count(project):
    sprints = Sprint.objects.filter(project=project).count()
    return sprints

@register.simple_tag
def get_task_count(project):

    tasks = Task.objects.filter(sprint__project=project).count()
    return tasks


