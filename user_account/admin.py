from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import User
from .import models





class UserAdmin(BaseUserAdmin):
   
    list_display = ('email', 'first_name', 'last_name',  'is_staff')
    #list_filter = ('country',  'state','city',)
    search_fields = ('email', 'first_name', 'last_name', )
    ordering = ('date_joined',)
    fieldsets = (  # this will be shown in the admin pannel
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ( # this will be need to add a user
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )



admin.site.register(User, UserAdmin)
admin.site.register(models.Email_varification)
