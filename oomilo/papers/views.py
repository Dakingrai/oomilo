from django.shortcuts import render
from .models import Paper

# Create your views here.

def home(request):
    return render(request, "papers/home.html")


def papers(request):
    papers = Paper.objects.all()
    context = {
        "papers": papers
    }
    return render(request, "papers/papers.html", context)
