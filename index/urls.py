from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'arena'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'auth/', views.process_user_signup, name='signup'),
    path(r'login/', views.user_login, name='login'),
    path(r'logout/', views.user_logout, name='logout'),
    path(r'dashboard/', include('dashboard.urls')),
    path(r'contact/', views.contact, name="contact"),
    path(r'ajax/validate_username', views.validate_username, name='validate_username'),
    path(r'eventcenter/', include("event_center.urls")),
]
