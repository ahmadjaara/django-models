from django.urls import path
from .views import SnackListView
#name for make a reference for that url or have two app and that have the same path
urlpatterns= [
    path("snack-list",SnackListView.as_view(),name="snack_list"),
    ]