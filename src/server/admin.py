from django.contrib.auth.admin import UserAdmin, UserChangeForm, UserCreationForm
from django.contrib.auth.models import AnonymousUser
from django.contrib import admin
from .models import (
    UdvUser,
    Article
)


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UdvUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UdvUser
        fields = ("email", "password", "first_name", "last_name")


class UdvUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
        (None, {'fields': ('password',)}),
        (('Personal info',), {'fields': ('first_name', 'last_name', 'email', 'occupation', 'age', 'is_moderator',)}),
        (('Permissions',), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates',), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    readonly_fields = ('first_name', 'last_name', 'email', 'occupation', 'age', 'is_active', 'is_staff', 'is_superuser',
                       'groups', 'user_permissions', 'last_login', 'date_joined',)

    def has_change_permission(self, request, obj=None):
        if request.user == AnonymousUser or (not request.user.is_staff and not request.user.is_superuser):
            return False
        if request.user.is_superuser or request.user.is_super_moderator:
            return True
        if obj is None:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user == AnonymousUser or (not request.user.is_staff and not request.user.is_superuser):
            return False
        if request.user.is_superuser:
            return True
        return False

    def has_module_permission(self, request):
        print(request.user.is_staff)
        if request.user == AnonymousUser or (not request.user.is_staff and not request.user.is_superuser):
            print("AAAAAAA")
            return False
        return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return self.readonly_fields


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'moderator',)

    def has_change_permission(self, request, obj=None):
        if request.user == AnonymousUser or (not request.user.is_staff and not request.user.is_superuser):
            return False
        if request.user.is_superuser:
            return True
        if not request.user.is_moderator:
            return False
        if obj is None:
            return True
        if request.user == obj.moderator or request.user.is_super_moderator:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user == AnonymousUser or (not request.user.is_staff and not request.user.is_superuser):
            return False
        if request.user.is_superuser:
            return True
        if obj is None:
            return False
        if request.user == obj.moderator:
            return True
        else:
            return False

    def has_module_permission(self, request):
        if request.user == AnonymousUser or (not request.user.is_staff and not request.user.is_superuser):
            return False
        return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        if obj is None:
            return self.readonly_fields
        if request.user == obj.moderator and request.user.is_super_moderator:
            self.readonly_fields = ('creator', 'parent', 'subscribers')
            return self.readonly_fields
        elif request.user == obj.moderator:
            self.readonly_fields = ('creator', 'parent', 'subscribers', 'moderator')
            return self.readonly_fields
        elif request.user.is_super_moderator:
            self.readonly_fields = ('creator', 'parent', 'subscribers', 'title', 'status', 'photos', 'terms', 'persons')
            return self.readonly_fields


admin.site.register(UdvUser, UdvUserAdmin)
admin.site.register(Article, ArticleAdmin)
