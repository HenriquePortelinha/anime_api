from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .anime import AnimeForm
from .character import CharacterForm
from .user import UserForm
from .models import Anime, Character

# View da página inicial
def home(request):
    return render(request, 'home.html')

# Lista de animes
def anime_list(request):
    animes = Anime.objects.all()
    return render(request, 'animes.html', {'animes': animes})

# Lista de personagens
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'characters.html', {'characters': characters})

# Registro de um novo anime
def register_anime(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animes')
    else:
        form = AnimeForm()
    return render(request, 'register_anime.html', {'form': form})

# Registro de um novo personagem
def register_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('characters')
    else:
        form = CharacterForm()
    return render(request, 'register_character.html', {'form': form})

# Registro de um novo usuário
def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

# Login do usuário
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Nome de usuário ou senha inválidos.')
    return render(request, 'login.html')

# Logout do usuário
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return HttpResponse('Você não está logado.')

# Busca de anime
def search_anime(request):
    query = request.GET.get('q')
    animes = Anime.objects.filter(name__icontains=query) if query else []
    return render(request, 'search_anime.html', {'animes': animes, 'query': query})

# Busca de personagem
def search_character(request):
    query = request.GET.get('q')
    characters = Character.objects.filter(name__icontains=query) if query else []
    return render(request, 'search_character.html', {'characters': characters, 'query': query})
