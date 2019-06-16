from django.contrib import admin
from .models import Music


class MusicAdmin(admin.ModelAdmin):
    model = Music
    list_display = (
        'id', 'reference_id', 'posted_by', 'label', 'artist', 'music_name', 'music_path', 'file_ext', 'label_image',
        'artist_image', 'is_active', 'visits', 'release_date', 'date_posted',
    )
    list_filter = ('label', 'artist', 'release_date')


admin.site.register(Music, MusicAdmin)
