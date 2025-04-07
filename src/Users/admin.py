from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModelAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "phone_no"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "phone_no", "password"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


class UserAddressesModelAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "id",
        "user",
        "first_name",
        "last_name",
        "email",
        "address_line_1",
        "address_line_2",
        "house_no",
        "street",
        "landmark",
        "state",
        "district",
        "country",
        "postal_code",
        "phone_no_1",
        "phone_no_2",
    )


# Now register the new UserAdmin...
admin.site.register(Users, UserModelAdmin)
admin.site.register(UserAddresses, UserAddressesModelAdmin)
