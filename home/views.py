from django.http import HttpResponse
from django.shortcuts import render

from home.models import Gallery

# Create your views here.

def home(request):

    gal_obj=Gallery.objects.all()

    return render(request,'index.html',{'gallery_obj':gal_obj})
