from django.urls import path

from .views import RoomListView, RoomDetailView, RoomCreateView

urlpatterns = [
    path('nueva-sala/', RoomCreateView.as_view(), name='room_new'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('', RoomListView.as_view(), name='room_list'),
]
