from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    pictures = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        
        fields = '__all__'
        
class JobSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        
        fields = '__all__'
        