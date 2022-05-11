from django.urls import path
from .views import SnackListView,SnackDetailView,Homepage
#name for make a reference for that url or have two app and that have the same path
urlpatterns= [
    path("",SnackListView.as_view(),name="snack_list"),
    path("detail-view/<int:pk>",SnackDetailView.as_view(),name="snack_detail"),
     
    ]