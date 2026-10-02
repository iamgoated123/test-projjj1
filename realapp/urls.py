from django.urls import path
from django.conf import settings
from . import views
from .views import get_user_profile_data

urlpatterns = [
    path('user_data/<str:pk>/', get_user_profile_data)
]
