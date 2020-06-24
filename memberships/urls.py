from django.urls import path
from . import views


urlpatterns = [
    path('', views.subscription_overview, name='subscription_overview'),
    path('', views.membership_list, name='membership_list'),
    path('payment/', views.payments, name='payments')
]
