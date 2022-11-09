from django.contrib import admin
from .models import Project, Job, Tag

# Register your models here.
admin.site.register(Project)
admin.site.register(Job)
admin.site.register(Tag)