from django.urls import path

from .views import RoomListView, RoomDetailView

urlpatterns = [
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('', RoomListView.as_view(), name='room_list'),
]
