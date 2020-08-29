from django.urls import path
# from django.conf.urls import include
from . import views
from index.views import validate_username as v_uname


app_name = "arena_event_center"

urlpatterns = [
    path('', views.index, name="event_center"),
    path('view-center', views.center, name="view_center"),
    path('ajax/validate_username', v_uname),
]
