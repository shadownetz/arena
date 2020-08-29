from django.contrib import admin
from .models import EventCenter, EventCenterReview


class EventCenterAdmin(admin.ModelAdmin):
    model = EventCenter
    list_display = [
        'id', 'owner', 'name', 'ref_id', 'category', 'phone', 'can_book', 'address',
        'availability', 'rating', 'website', 'country', 'state',
        'image_rep', 'date_history', 'date_registered'
    ]

    list_filter = ['owner', 'can_book', 'rating']


class ReviewAdmin(admin.ModelAdmin):
    model = EventCenterReview
    list_display = [
        'id', 'user', 'model', 'comment', 'likes', 'dislikes', 'date_created'
    ]

    list_filter = ['likes', 'dislikes', 'date_created']


admin.site.register(EventCenter, EventCenterAdmin)
admin.site.register(EventCenterReview, ReviewAdmin)
