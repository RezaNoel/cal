from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('panel', views.panel),
    path('projects/', views.project_list_view, name='project_list_view'),
    path('projects/<int:project_id>/', views.project_detail_view, name='project_detail_view'),
    path('projects/<int:project_id>/sprints/', views.sprint_list_view, name='sprint_list_view'),
    path('projects/<int:project_id>/sprints/<int:sprint_id>/', views.sprint_detail_view, name='sprint_detail_view'),
    path('projects/<int:project_id>/sprints/<int:sprint_id>/tasks/', views.task_list_view, name='task_list_view'),
    path('projects/<int:project_id>/sprints/<int:sprint_id>/tasks/create/', views.create_task_view, name='create_task_view'),
    path('projects/<int:project_id>/sprints/<int:sprint_id>/tasks/<int:task_id>/', views.task_detail_view, name='task_detail_view'),
    path('projects/<int:project_id>/sprints/<int:sprint_id>/tasks/<int:task_id>/edit/', views.edit_task_view, name='edit_task_view'),
    path('projects/<int:project_id>/sprints/<int:sprint_id>/tasks/<int:task_id>/delete/', views.delete_task_view, name='delete_task_view'),
    path('projects/create/', views.create_project_view, name='create_project_view'),
    path('projects/<int:project_id>/edit/', views.edit_project_view, name='edit_project_view'),
    path('projects/<int:project_id>/delete/', views.delete_project_view, name='delete_project_view'),
    path('projects/<int:project_id>/sprints/create/', views.create_sprint_view, name='create_sprint_view'),
    path('projects/<int:project_id>/sprints/<int:sprint_id>/edit/', views.edit_sprint_view, name='edit_sprint_view'),
    path('projects/<int:project_id>/sprints/<int:sprint_id>/delete/', views.delete_sprint_view, name='delete_sprint_view'),
]

