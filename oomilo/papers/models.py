from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

PAPER_CATEGORIES = (
    ("FEATURE", "Feature"),
    ("CIRCUIT", "Circuit"),
    ("UNIVERSALITY", "Universality"),
    ("TECHNIQUES", "Techniques"),
    ("OTHER", "Other")
)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Paper(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    url = models.URLField(max_length = 500)
    category = MultiSelectField(choices=PAPER_CATEGORIES)
    notes = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    Project = models.ManyToManyField(Project, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
