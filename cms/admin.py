from django.contrib import admin
from .models import Task,Sprint,Project,Attachment
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Sprint)
admin.site.register(Attachment)