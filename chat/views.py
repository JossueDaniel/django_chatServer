from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room


# Create your views here.
class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'home.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(owner=self.request.user)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_rooms'] = Room.objects.all()
        return context


class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'room_detail.html'


class RoomCreateView(CreateView):
    model = Room
    fields = ['name', 'owner']
    template_name = 'room_new.html'
