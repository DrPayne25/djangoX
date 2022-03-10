from django.urls import path
from .views import GameCreateView, GameDeleteView, GameDetailView, GameListView, GameUpdateView

urlpatterns = [
  path('', GameListView.as_view(), name='game_list'),
  path('<int:pk>/', GameDetailView.as_view(), name='game_detail'),
  path('new/', GameCreateView.as_view(), name='game_create'),
  path('<int:pk>/edit', GameUpdateView.as_view(), name='game_update'),
  path('<int:pk>/delete', GameDeleteView.as_view(), name='game_delete'),
]
