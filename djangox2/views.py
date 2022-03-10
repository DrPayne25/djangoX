from django.shortcuts import render
from .models import Game
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class GameListView(ListView):
  template_name = 'djangox2/game-list.html'
  model = Game

class GameDetailView(DetailView):
  template_name = 'djangox2/game-detail.html'
  model = Game

class GameCreateView(CreateView):
  template_name = 'djangox2/game-create.html'
  model = Game
  fields = ['title', 'developer', 'description']

class GameUpdateView(UpdateView):
  template_name = 'djangox2/game-update.html'
  model = Game
  fields = ['title', 'developer', 'description']

class GameDeleteView(DeleteView):
  template_name = 'djangox2/game-delete.html'
  model = Game
  success_url = reverse_lazy('game_list')




