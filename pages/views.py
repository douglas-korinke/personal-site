from django.shortcuts import render
from .models import Menu
from .models import Project


def index(request):
    projects = Project.objects.all().order_by("-created_at")
    return render(request, "pages/index.html", {"projects": projects})


def menu(request):
    menu = Menu.objects.all()
    return render(request, "base.html", {"menu": menu})
