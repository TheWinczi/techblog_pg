from django.contrib import admin
from django.utils.translation import gettext as _

from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('General'), {'fields': ['email', 'password']}),
        (_('Account'), {'fields': ['is_staff', 'is_active', 'groups']}),
    ]
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email',)
    search_fields = ('email',)
    ordering = ('email', 'is_staff', 'is_active')


admin.site.register(CustomUser, CustomUserAdmin)
