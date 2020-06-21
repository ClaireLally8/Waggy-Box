from django.urls import path
from . import views


urlpatterns = [
    path('', views.member_type, name='membership_type'),
]
