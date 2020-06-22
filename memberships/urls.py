from django.urls import path
from . import views


urlpatterns = [
    path('', views.membership_list, name='membership_list'),
    path('payment/', views.selected_membership, name='selected_membership'),
]
