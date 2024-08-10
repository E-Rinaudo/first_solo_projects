#!/usr/bin/env python3

"""
This module defines the 'Sound' class to manage the game's audio.

It handles initialization and playback of sound effects, such as hero firing,
alien explosion, and game-over sounds.
It also manages background music, selecting and playing tracks from a list.
"""

from random import choice

import pygame


class Sound:
    """A Class to manage the sounds of the game."""

    def __init__(self):
        """Initialize the sounds."""
        pygame.mixer.init()

        # Sounds for alien explosion and game over.
        self.alien_explosion = pygame.mixer.Sound("sounds/explosion.wav")
        self.alien_explosion.set_volume(0.3)
        self.hero_fire = None

        self.end_game = pygame.mixer.Sound("sounds/end.wav")

    def background_music(self):
        """Initialize the background music."""
        # Randomly choose a background song.
        background_list = [
            "sounds/background1.mp3.ogg",
            "sounds/background2.ogg",
            "sounds/background3.ogg",
            "sounds/background4.ogg",
            "sounds/background5.ogg",
        ]
        background = choice(background_list)

        pygame.mixer.music.load(background)
        pygame.mixer.music.set_volume(0.4)

    def hero_bullet_sound(self):
        """Randomly choose a sound for the hero firing."""
        hero_fire_list = ["sounds/laser1.wav", "sounds/laser2.wav", "sounds/laser3.wav"]
        hero_firing = choice(hero_fire_list)

        self.hero_fire = pygame.mixer.Sound(hero_firing)
        self.hero_fire.set_volume(0.6)
