from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Sprint(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    status = models.CharField(max_length=255)  # Options: To-Do, In Progress, Done
    due_date = models.DateField()
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    assigned_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
