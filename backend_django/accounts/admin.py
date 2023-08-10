from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import COOPUser

@admin.register(COOPUser)
class COOPUserAdmin(UserAdmin):
    exclude = ('date_joined',)

    # Define admin model for custom user with some overridden methods
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'deposit_number', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'deposit_number')
    ordering = ('email',)

    # Override the fieldsets to not include 'username'
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'deposit_number')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login',)}),  # Removed 'date_joined' since you excluded it
    )

    # Update 'add_fieldsets' to not include 'username'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
