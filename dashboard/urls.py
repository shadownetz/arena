from django.urls import path
from . import views

app_name = 'arena_dashboard'

urlpatterns = [
    path('', views.index, name="index"),
    path(r'profile/', views.user_profile, name="profile"),
    path(r'profile/ajax/update_profile/', views.update_profile, name="update-profile"),
    path(r'profile/ajax/get_profile/', views.profile_data_request, name="profile_request"),
    path(r'add_event/', views.add_event_center, name='addEventCenter'),
    path(r'process_add_event/', views.process_add_new_event_center, name="process_add_new_event_center"),
    path(r'modify_event_center', views.modify_event_center, name='modifyEventCenter'),
    path(r'all_event_center/', views.view_all_event_center, name='viewAllEventCenter'),
    path(r'add_food_drink', views.add_new_food_drink, name='addFoodDrink'),
    path(r'process_add_food_drink', views.process_add_new_food_drink, name='process_addFoodDrink'),
    path(r'all_food_drink', views.view_all_food_drink_item, name='viewAllFoodDrinkItem'),
    path(r'modify_food_drink/', views.modify_food_drink_item, name='modifyFoodDrink'),
    path(r'add_restaurant', views.add_restaurant, name='addRestaurant'),
    path(r'process_add_restaurant', views.process_add_restaurant, name='process_addRestaurant'),
    path(r'all_restaurants/', views.view_all_restaurants, name='viewAllRestaurants'),
    path(r'modify_restaurant/', views.modify_restaurant, name='modifyRestaurant')
]
