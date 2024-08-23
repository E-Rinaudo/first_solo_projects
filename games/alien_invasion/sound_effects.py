#!/usr/bin/env python3

"""
This module defines the 'Sound' class to manage the game's audio.

It handles initialization and playback of sound effects, such as ship firing,
alien explosion, and game-over sounds.
It also manages background music, selecting and playing tracks from a list.
"""

from random import choice

import pygame


class Sound:  # pylint: disable=R0903
    """A Class to manage the sounds of the game."""

    def __init__(self) -> None:
        """Initialize the sounds."""
        pygame.mixer.init()

        # Sounds for ship firing, alien explosion and game over.
        self.ship_fire: pygame.mixer.Sound = pygame.mixer.Sound("sounds/laser.wav")
        self.ship_fire.set_volume(0.7)

        self.alien_explosion: pygame.mixer.Sound = pygame.mixer.Sound(
            "sounds/explosion.wav"
        )
        self.alien_explosion.set_volume(0.3)

        self.end_game: pygame.mixer.Sound = pygame.mixer.Sound("sounds/end.wav")

    def background_music(self) -> None:
        """Initialize the background music."""
        # Randomly choose a background song.
        background_list: list[str] = [
            "sounds/background1.wav",
            "sounds/background2.ogg",
            "sounds/background3.mp3",
            "sounds/background4.mp3",
        ]
        background: str = choice(background_list)

        pygame.mixer.music.load(background)
        pygame.mixer.music.set_volume(0.4)
