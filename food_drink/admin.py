from django.contrib import admin
from .models import FoodDrink, FoodDrinkReview


class FoodDrinkAdmin(admin.ModelAdmin):
    model = FoodDrink
    list_display = [
        'id', 'category', 'ref_id', 'name', 'ingredients', 'rating',
        'assoc_country', 'assoc_states', 'image_rep', 'date_registered'
    ]

    list_filter = ['rating']


class ReviewAdmin(admin.ModelAdmin):
    model = FoodDrinkReview
    list_display = [
        'id', 'user', 'model', 'comment', 'likes', 'dislikes', 'date_created'
    ]

    list_filter = ['likes', 'dislikes', 'date_created']


admin.site.register(FoodDrink, FoodDrinkAdmin)
admin.site.register(FoodDrinkReview, ReviewAdmin)
