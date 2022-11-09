from django.shortcuts import render
from .serializers import ProjectSerializer, JobSerializer, TagSerializer
from .models import Project, Job, Tag
from rest_framework import viewsets

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by('-date')
    
class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all().order_by('-date_to')
    
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

# Tag filtered viewsets.
class FilteredViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        tag_type = self.request.get_full_path().replace("api/projects/", "").replace("/", "")
        
        print(self.request.GET.get('q', ''))
        
        type_id = Tag.objects.get(name=tag_type).id

        queryset = Project.objects.all().filter(tags__id=type_id).order_by('-date')

        return queryset