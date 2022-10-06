from django.shortcuts import render,redirect

from seller.models import *

# Create your views here.

def sellerindex(request):
    return render(request,'sellerindex.html')

def sellerlogin(request):
    if request.method=='POST':
        try:
            Seller.objects.get(email=request.POST['email'])
            return redirect('sellerindex')
        except:
            return render(request,'login.html',{'msg':'User not found'})
    return render(request,'sellerlogin.html')

def addproduct(request):
    if request.method=='POST':
        Product.objects.create(           
            name=request.POST['name'],
            des=request.POST['des'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            discount=request.POST['discount'],          
        )
    return render(request,'addproduct.html')