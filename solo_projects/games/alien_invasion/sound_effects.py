from random import choice

import pygame


class Sound:
    """A Class to manage the sounds of the game."""

    def __init__(self):
        """Initialize the sounds."""
        pygame.mixer.init()

        # Sounds for ship firing, alien explosion and game over.
        self.ship_fire = pygame.mixer.Sound("sounds/laser.wav")
        self.ship_fire.set_volume(0.7)

        self.alien_explosion = pygame.mixer.Sound("sounds/explosion.wav")
        self.alien_explosion.set_volume(0.3)

        self.end_game = pygame.mixer.Sound("sounds/end.wav")

    def background_music(self):
        """Initialize the background music."""
        # Randomly choose a background song.
        background_list = [
            "sounds/background1.wav",
            "sounds/background2.ogg",
            "sounds/background3.mp3",
            "sounds/background4.mp3",
        ]
        background = choice(background_list)

        pygame.mixer.music.load(background)
        pygame.mixer.music.set_volume(0.4)
