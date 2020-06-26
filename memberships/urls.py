from django.urls import path
from . import views


urlpatterns = [
    path('', views.sub_overview, name='sub_overview'),
    path('types/', views.membership_list, name='membership_list'),
    path('payment/', views.payments, name='payments'),
    path('cancel/', views.cancelSubscription, name='cancelSubscription'),
]
