from django.shortcuts import render,redirect

from myapp.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email'])
            return redirect('index')
        except:
            return render(request,'login.html',{'msg':'User not found'})
        
    return render(request,'login.html')