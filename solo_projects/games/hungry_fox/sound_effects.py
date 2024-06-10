from random import choice

import pygame


class Sound:
    """A Class to manage the sounds of the game."""

    def __init__(self):
        """Initialize the sounds."""
        pygame.mixer.init()
        
        # Sounds for fox firing, farmer death and game over.
        self.fox_fire = pygame.mixer.Sound('sounds/throw.wav')
        self.fox_fire.set_volume(0.7)

        self.farmer_death = pygame.mixer.Sound('sounds/farmer_death.ogg')

        self.end_game = pygame.mixer.Sound('sounds/end.mp3')
    
    def background_music(self):
        """Initialize the background music."""
        # Randomly choose a background song.
        background_list = ['sounds/background1.wav', 'sounds/background2.ogg']
        background = choice(background_list)
        
        pygame.mixer.music.load(background)
        pygame.mixer.music.set_volume(0.4)