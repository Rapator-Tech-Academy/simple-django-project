from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import UserDevice

User = get_user_model()

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'surname', 'is_active']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    list_editable = ['name', 'surname', 'is_active']
    search_fields = ['name', 'surname', 'email', 'device__device_name']

""" 

Sabuhi 

buh => User.objects.filter(name__icontains="buh")

"""

admin.site.register(UserDevice)