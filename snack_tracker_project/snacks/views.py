from django.shortcuts import render
from django.views.generic import ListView ,DeleteView,TemplateView
from .models import Snack
# Create your views here.

class SnackListView (ListView):
    template_name="snack_list.html"
    model =Snack
     
class SnackDetailView(DeleteView):
    template_name="snack_detail.html"
    model=Snack

class Homepage(TemplateView):
    template_name='home.html'