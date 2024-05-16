from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room


# Create your views here.
class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'home.html'


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'room_detail.html'
