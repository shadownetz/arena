from django.urls import path
from . import views

app_name = 'arena_dashboard'

urlpatterns = [
    path('', views.index, name="index"),
    path(r'profile/', views.user_profile, name="profile"),
    path(r'su/', views.su_index, name='su'),
    path(r'su/profile/', views.su_user_profile, name="suProfile"),
    path(r'profile/ajax/update_profile/', views.update_profile, name="update-profile"),
    path(r'profile/ajax/get_profile/', views.profile_data_request, name="profile_request")
]
