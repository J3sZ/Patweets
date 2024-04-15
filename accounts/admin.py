from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here my friend :).
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "id",
        "email",
        "username",
        "nickname",
        "age",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("age", "nickname", "bio")}), )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields" : ("age", "nickname", "bio")}), )

admin.site.register(CustomUser, CustomUserAdmin)