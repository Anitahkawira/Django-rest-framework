from django.shortcuts import render
from .models import Course
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import CourseSerializer

# Create your views here.
def welcome(request):
    return render(request, 'index.html')
    
def courses (request):
    courses = Course.objects.all()
    context ={
        'courses':courses
    }
    return render(request, 'index.html', context)
    
# ViewSets define the view behavior.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
