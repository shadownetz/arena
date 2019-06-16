from django.contrib import admin
from .models import Info


class InfoAdmin(admin.ModelAdmin):
    model = Info
    list_display = (
        'id', 'reference_id', 'post_by', 'category', 'heading', 'content',
        'post_image', 'tags', 'is_active', 'visits', 'date_posted'
    )
    list_filter = ('category', 'tags', 'date_posted')


admin.site.register(Info, InfoAdmin)
