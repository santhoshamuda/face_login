from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Face Recognition', {'fields': ('face_encoding',)}),
    )
    readonly_fields = ['face_encoding']

admin.site.register(CustomUser, CustomUserAdmin)
