from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('products/',views.products,name='products'),
    path('single/<int:pid>',views.single,name='single'),
]
