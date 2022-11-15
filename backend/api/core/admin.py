from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication', 'show')

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Job)
admin.site.register(Tag)
admin.site.register(Image)