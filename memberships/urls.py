from django.urls import path
from . import views


urlpatterns = [
    path('membertype', views.Membership, name='Membership_Type'),
]
