# api_anime/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'), 
    path('animes', views.anime_list, name='animes'),
    path('characters', views.character_list, name='characters'),
    path('register_anime', views.register_anime, name='register_anime'),
    path('register_character', views.register_character, name='register_character'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('search_anime', views.search_anime, name='search_anime'),
    
]
