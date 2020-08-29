from django.contrib import admin
from .models import (Profile, Archive, Message)


class CustomArchiveAdmin(admin.ModelAdmin):
    model = Archive
    list_display = ('id', 'username', 'email', 'date_created', 'date_deleted')
    list_filter = ('username', 'email', 'date_deleted')


class ProfilesAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('id', 'user', 'phone_number', 'nick_name', 'shipping_addr', 'about')
    list_filter = ('user',)


class MessageAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('id', 'user', 'heading', 'content', 'category', 'is_read', 'timestamp')
    list_filter = ('user', 'category', 'timestamp')


admin.site.register(Profile, ProfilesAdmin)
admin.site.register(Archive, CustomArchiveAdmin)
admin.site.register(Message, MessageAdmin)
