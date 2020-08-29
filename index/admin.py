from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ModelEditProfile, ModelSignUp
from .models import (UserProfile, Log, UserImage, ImageGallery)
# from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    add_form = ModelSignUp
    form = ModelEditProfile
    model = UserProfile
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'avatar', 'date_created')
    list_filter = ('username', 'email', 'is_staff', 'is_active', 'date_created',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('username', 'password', 'email',)
                }),
        ('Permissions', {'fields': ('is_staff', 'is_active',)})
    )
    search_fields = ('username',)
    ordering = ('date_created',)


class CustomLogAdmin(admin.ModelAdmin):
    model = Log
    list_display = ('user', 'category', 'message', 'timestamp')
    list_filter = ('user', 'category', 'timestamp')


class UserImageAdmin(admin.ModelAdmin):
    model = UserImage
    list_display = ('username', 'image_path',)
    list_filter = ('username',)


class AllImagesAdmin(admin.ModelAdmin):
    model = ImageGallery
    list_display = ('id', 'ref_id', 'image', 'uploaded')
    list_filter = ('uploaded',)


admin.site.register(UserProfile, CustomUserAdmin)
admin.site.register(Log, CustomLogAdmin)
admin.site.register(UserImage, UserImageAdmin)
admin.site.register(ImageGallery, AllImagesAdmin)
