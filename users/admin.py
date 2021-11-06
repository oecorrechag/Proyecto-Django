""" User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    # esto es lo que sale en la pagina admin
    list_display = ('pk','user','phone_number','website','picture')
    # esto se vuelve links
    list_display_links = ('pk','user')
    # esto se vuelve editable desde la pagina admin
    list_editable = ('phone_number','website','picture')
    # variables para buscar
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    # filtros de busqueda
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    #
    fieldsets = (
        ('Profile',{
            'fields':(('user', 'picture'),),
        }),
        ('Extra Info',{
            'fields':(
                ('phone_number','website'),
                ('biography')
                )
        }),
        ('Metadata',{
            'fields':(
                ('created','modified'),)
        })
    )

    readonly_fields = ('created','modified')

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for user."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)