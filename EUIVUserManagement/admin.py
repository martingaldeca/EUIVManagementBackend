# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from EUIVUserManagement.models import EuIVUser, EuIVUserActiveGames, EuIVUserProfile


class UserActiveGamesInline(admin.TabularInline):
    model = EuIVUserActiveGames
    verbose_name_plural = 'User active games'


class ProfileInline(admin.StackedInline):
    model = EuIVUserProfile
    can_delete = False
    verbose_name_plural = 'Profile'


@admin.register(EuIVUser)
class EuIVUserAdmin(UserAdmin):
    model = EuIVUser
    inlines = (UserActiveGamesInline, ProfileInline)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(EuIVUserAdmin, self).get_inline_instances(request, obj)
