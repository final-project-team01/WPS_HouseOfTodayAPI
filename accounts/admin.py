from django.contrib import admin
from .models import User

# Register your models here.
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
   UserAdmin.fieldsets[1][1]['fields']+=('gender','birthday','profile','message')

   UserAdmin.add_fieldsets += (
       (('Additional Info'), {'fields':('gender','birthday','profile','message')}),
   )

admin.site.register(User, CustomUserAdmin)