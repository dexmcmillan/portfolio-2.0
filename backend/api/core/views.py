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
        