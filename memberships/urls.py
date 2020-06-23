from django.urls import path
from . import views


urlpatterns = [
    path('', views.membership_list, name='membership_list'),
    path('payment/', views.payments, name='payments'),
    path('update-membership/<subscription_id>/', views.update_membership, name='update_membership'),
]
