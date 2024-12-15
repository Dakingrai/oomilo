from django.shortcuts import render
from .models import Paper, Tag
import pdb
# Create your views here.

def home(request):
    return render(request, "papers/home.html")


def papers(request):
    papers = Paper.objects.all()
    context = {
        "papers": papers
    }
    return render(request, "papers/papers.html", context)

def tags(request):
    tags = Tag.objects.all()
    context = {
        "tags": tags
    }
    return render(request, "papers/tags.html", context)

def tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    papers_with_tag = tag.paper_set.all()
    context = {
        "papers": papers_with_tag
    }
    return render(request, "papers/tag.html", context)
