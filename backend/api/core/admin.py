from django.contrib import admin
from .models import Project, Job, Tag

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication', 'show')

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Job)
admin.site.register(Tag)