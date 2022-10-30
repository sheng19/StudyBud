import imp
from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.get_routers),
    path('api/rooms', views.get_rooms),
    path('api/rooms/<str:pk>', views.get_room),
]
