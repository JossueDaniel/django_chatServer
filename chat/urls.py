from django.urls import path

from .views import RoomListView, RoomDetailView, RoomCreateView, RoomDeleteView

urlpatterns = [
    path('<int:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),
    path('nueva-sala/', RoomCreateView.as_view(), name='room_new'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('', RoomListView.as_view(), name='room_list'),
]
