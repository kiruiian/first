from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def index(request):
    all_students = Student.objects.all()
    return render(request, "index.html", {"All": all_students})
