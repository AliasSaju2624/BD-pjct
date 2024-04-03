from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404,reverse,HttpResponse
from django.core.files.storage import FileSystemStorage
from main.models import registration
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        print(name)
        password=request.POST.get('password')
        print(password)
        password2=request.POST.get('password2')
        print(password2)
        user=registration.objects.filter(name=name)
        if user:
            userdetails=registration.objects.get(name=name)
            messages.info(request, 'User already exist')
            return render(request,'registration.html')
        elif name =='':
            messages.info(request, 'Please provide name')
            return render(request,'registration.html')
        elif password =='':
            messages.info(request, 'Please password ')
            return render(request,'registration.html')
        elif password2 =='':
            messages.info(request, 'Please password ')
            return render(request,'registration.html')
        else:
            if (password==password2):
                registration(name=name,password=password).save()
                return render(request,'login.html')
            else:
            # context = "password not match"
                messages.info(request, 'Password does not match!')
                return render(request,'registration.html')
    else:
        return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user=registration.objects.filter(name=name,password=password)
        if user:
            userdetails=registration.objects.get(name=name,password=password)
            id=userdetails.id
            request.session['id']=id
            return redirect('login')
    return render(request,'login.html')