from django.shortcuts import render,redirect

from myapp.models import Cart, User
from seller.models import *
from django.http import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email'])
            request.session['email']=request.POST['email']
            return redirect('index')
        except:
            return render(request,'login.html',{'msg':'User not found'})
        
    return render(request,'login.html')

def products(request):
    plist=Product.objects.all()
    for item in plist:
        item.discountedprice=item.price-(item.price*item.discount/100)
    return render(request,'products.html',{'plist':plist})

def single(request,pid):
    pobj=Product.objects.get(id=pid)
    pobj.discountedprice=pobj.price-(pobj.price*pobj.discount/100)
    return render(request,'single.html',{'pobj':pobj})

def addtocart(request):
    pid=request.GET['pid']
    userobj = User.objects.get(email=request.session['email'])
    pobj = Product.objects.get(id=pid)

    Cart.objects.create(
        product=pobj,
        user=userobj,
        quantity=1
    )
    return JsonResponse({'msg':'Product Added to cart.'})