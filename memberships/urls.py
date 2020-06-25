from django.urls import path
from . import views


urlpatterns = [
    path('types/', views.membership_list, name='membership_list'),
    path('payment/', views.payments, name='payments')
]
