from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','password']

@admin.register(Cart)
class UserAdmin(admin.ModelAdmin):
    list_display=['product','quantity','user']