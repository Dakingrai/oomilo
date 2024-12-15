from django.contrib import admin
from .models import Paper, Tag, Project

# Register your models here.
admin.site.register(Tag)

class PaperAdmin(admin.ModelAdmin):
  list_display = ("name", "category")
  
admin.site.register(Paper, PaperAdmin)
admin.site.register(Project)

