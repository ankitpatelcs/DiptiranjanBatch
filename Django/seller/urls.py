from django.urls import path
from . import views

urlpatterns = [
    path('sellerindex/',views.sellerindex,name='sellerindex'),
    path('',views.sellerlogin,name='sellerlogin'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('manageproducts/',views.manageproducts,name='manageproducts')
]
