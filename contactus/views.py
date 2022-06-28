from django.http import HttpResponse
from django.shortcuts import render
from .models import Message


# Create your views here.

def contactus(request):

    if request.method == 'POST':

        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        if name == ' ' or email == ' ' or subject == ' ' or message == ' ':
            return HttpResponse("<script>alert('please fill all input fields!'); window.open('/contactus','_self');</script>")
        else:   
            new_message = Message(name=name,email=email,subject=subject,message=message)
            new_message.save()  
            return HttpResponse("<script>alert('message send!'); window.open('/contactus','_self');</script>")
    
    return render(request,'contactus.html',{})

