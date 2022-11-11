from rest_framework import serializers
from .models import Project, Job, Tag

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        
        fields = ("id", "name",)

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        
        fields = ("id", "title", "date", "publication", "description", "embed", "link", "picture", "tags", "show")
        
class JobSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        
        fields = ("id", "title", "date_from", "date_to", "org", "accomplishments", "current", "tags")
        