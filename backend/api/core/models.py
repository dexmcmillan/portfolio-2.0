from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.name)

class Project(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField()
    publication = models.CharField(max_length=40)
    description = models.TextField(max_length=10000)
    embed = models.TextField(max_length=10000, blank=True)
    link = models.CharField(max_length=200, default="", blank=True)
    picture = models.FileField(blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title)
    
    
class Job(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    org = models.CharField(max_length=50, null=True, blank=True)
    accomplishments = models.TextField(max_length=100000)
    current = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.org)