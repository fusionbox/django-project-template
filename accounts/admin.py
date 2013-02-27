from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from accounts.forms import UserCreationForm, UserChangeForm
from accounts.models import User


class UserAdmin(DjangoUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_filter = ('is_superuser', 'is_active')
    list_display = ('email', 'name', 'is_superuser', 'is_active', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at', 'is_staff')
    date_hierarchy = 'created_at'
    ordering = ('email',)
    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            (_('Personal info'), {'fields': ('name',)}),
            (_('Permissions'), {'fields': ('is_active', 'is_superuser')}),
            (_('Important dates'), {'fields': ('created_at', 'updated_at')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    filter_horizontal = tuple()

admin.site.register(User, UserAdmin)
