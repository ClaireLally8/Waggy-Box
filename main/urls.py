from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('shop/', views.shop, name='shop'),
<<<<<<< HEAD
    path('shop/<item_id>', views.shop_item, name='shop_item'),
=======
    path('<item_id>', views.shop_item, name='shop_item'),
>>>>>>> 6dd786a17170179395c8ffa48b44a22b09668ff3
]
