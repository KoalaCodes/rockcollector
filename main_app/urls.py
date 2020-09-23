from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rocks/', views.rocks_index, name='rocks'),
    path('rocks/<int:rock_id>/', views.rocks_detail, name='rocks_detail')
    path('rocks/<int:rock_id>/add_polished/', views.add_polished, name='add_polished'),
    path('rocks/<int:rock_id>/add_photo/', views.add_photo, name='add_photo'),
    path('rocks/<int:rock_id>/assoc_color/<int:color_id', views.assoc_color, name='assoc_color),
    path('rocks/create/', views.RockCreate.as_view(), name='rocks_create'),
    path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
    path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'),
    path('colors/', views.colors_index, name='colors'),
    path('colors/<int:color_id>/', views.colors_detail, name='colors_detail'),
    path('colors/create/', views.ColorCreate.as_view(), name='colors_create'),
    path('colors/<int:pk>/update/', views.ColorUpdate.as_view(), name='colors_update'),
    path('colors/<int:pk>/delete/', views.ColorDelete.as_view(), name='colors_delete'),
    path('accounts/signup', views.signup, name='signup'),
]