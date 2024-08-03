"""
This module defines the 'Sound' class to manage the game's audio.

It handles initialization and playback of sound effects, such as penguin firing,
orca deaths, and game-over sounds.
It also manages background music, selecting and playing tracks from a list.
"""


from random import choice

import pygame


class Sound:
    """A Class to manage the sounds of the game."""

    def __init__(self):
        """Initialize the sounds."""
        pygame.mixer.init()

        # Sounds for penguin firing, orca death and game over.
        self.penguin_fire = pygame.mixer.Sound("sounds/throw.ogg")
        self.penguin_fire.set_volume(0.7)

        self.orca_death = pygame.mixer.Sound("sounds/orca_death.ogg")
        self.orca_death.set_volume(0.3)

        self.end_game = pygame.mixer.Sound("sounds/end.wav")

    def background_music(self):
        """Initialize the background music."""
        # Randomly choose a background song.
        background_list = [
            "sounds/background1.ogg",
            "sounds/background2.ogg",
            "sounds/background3.wav",
            "sounds/background4.ogg",
        ]
        background = choice(background_list)

        pygame.mixer.music.load(background)
        pygame.mixer.music.set_volume(0.4)
