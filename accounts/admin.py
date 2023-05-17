from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets =UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'tel','user_image'
            ),
        }),
    )
    


admin.site.register(CustomUser,CustomUserAdmin)
