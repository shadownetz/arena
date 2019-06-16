from django.contrib import admin
from .models import Software


class SoftwareAdmin(admin.ModelAdmin):
    model = Software
    list_display = ('id', 'reference_id', 'version', 'category', 'file', 'file_ext', 'visits', 'tags', 'uploaded')
    list_filter = ('reference_id', 'category', 'version', 'uploaded')


admin.site.register(Software, SoftwareAdmin)
