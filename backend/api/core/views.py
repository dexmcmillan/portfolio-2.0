from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().filter(show=True).order_by('-date')
    
class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all().order_by('-date_to')
    
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    
class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()