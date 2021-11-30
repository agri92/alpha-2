from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from myapp.models import CustomUser
# Register your models here.

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)

admin.site.site_header = "Alpha Master - Instituto de inglés"
admin.site.site_title = "Alpha Master"
admin.site.index_title = "Panel de administración"