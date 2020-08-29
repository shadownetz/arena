from django.contrib import admin
from .models import Restaurant, RestaurantReview


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = [
        'id', 'owner', 'name', 'ref_id', 'category', 'has_extras', 'can_book', 'can_place_order',
        'can_make_home_delivery', 'address', 'phone', 'country', 'state', 'rating',
        'open_time', 'close_time', 'image_rep', 'date_history', 'date_registered'
    ]

    list_filter = ['owner', 'has_extras', 'rating']


class ReviewAdmin(admin.ModelAdmin):
    model = RestaurantReview
    list_display = [
        'id', 'user', 'model', 'comment', 'likes', 'dislikes', 'date_created'
    ]

    list_filter = ['likes', 'dislikes', 'date_created']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantReview, ReviewAdmin)
