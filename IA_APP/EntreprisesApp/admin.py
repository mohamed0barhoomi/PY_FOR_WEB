from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Entreprise, Utilisateur


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    ordering = ("email",)
    list_display = ("user_id", "email", "first_name", "last_name", "role", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    readonly_fields = ("user_id", "last_login", "date_joined")
    fieldsets = (
        (None, {"fields": ("user_id", "email", "password")}),
        ("Informations personnelles", {"fields": ("first_name", "last_name", "telephone", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Dates importantes", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "telephone", "role", "password1", "password2"),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change and not obj.user_id:
            obj.user_id = Utilisateur.objects._generate_user_id()
        super().save_model(request, obj, form, change)


admin.site.register(Entreprise)
