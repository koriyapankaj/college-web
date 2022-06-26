from django.shortcuts import render

from course.models import Course

# Create your views here.

def bca(req):
    course_obj=Course.objects.all()[0]

    return render(req,'course.html',{'c_obj':course_obj})



def mca(req):
    course_obj=Course.objects.all()[1]

    return render(req,'course.html',{'c_obj':course_obj})