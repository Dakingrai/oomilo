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

class Paper(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField(max_length = 500)
    category = MultiSelectField(choices=PAPER_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
