from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Game


class gameTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.game = Game.objects.create(
            title="Mario", developer=self.user, description="worse than you think",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.game), "Mario")
    
    def test_string_representation_not_working(self):
        self.assertNotEqual(str(self.game), "Marios")

    def test_game_content(self):
        self.assertEqual(f"{self.game.title}", "Mario")
        self.assertEqual(f"{self.game.developer}", "tester@email.com")
        self.assertEqual(f"{self.game.description}", "worse than you think")
    
    def test_game_not_content(self):
        self.assertNotEqual(f"{self.game.title}", "Marios")
        self.assertNotEqual(f"{self.game.developer}", "testers")
        self.assertNotEqual(f"{self.game.description}", "better than you think")
