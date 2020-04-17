# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from EUIVUserManagement.models import EuIVUser, EuIVUserActiveGames
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = EuIVUser
        fields = UserCreationForm.Meta.fields + ('user_type',)


class UserActiveGamesInline(admin.TabularInline):
    model = EuIVUserActiveGames
    verbose_name_plural = 'User active games'


@admin.register(EuIVUser)
class EuIVUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    model = EuIVUser
    inlines = (UserActiveGamesInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_type')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('user_type',),
        }),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(EuIVUserAdmin, self).get_inline_instances(request, obj)
