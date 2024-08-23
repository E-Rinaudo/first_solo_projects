#!/usr/bin/env python3

"""
This module defines the 'Sound' class to manage the game's audio.

It handles initialization and playback of sound effects, such as fox firing,
farmer death, and game-over sounds.
It also manages background music, selecting and playing tracks from a list.
"""

from random import choice

import pygame


class Sound:  # pylint: disable=R0903
    """A Class to manage the sounds of the game."""

    def __init__(self) -> None:
        """Initialize the sounds."""
        pygame.mixer.init()

        # Sounds for fox firing, farmer death and game over.
        self.fox_fire: pygame.mixer.Sound = pygame.mixer.Sound("sounds/throw.wav")
        self.fox_fire.set_volume(0.7)

        self.farmer_death: pygame.mixer.Sound = pygame.mixer.Sound(
            "sounds/farmer_death.ogg"
        )
        self.end_game: pygame.mixer.Sound = pygame.mixer.Sound("sounds/end.mp3")

    def background_music(self) -> None:
        """Initialize the background music."""
        # Randomly choose a background song.
        background_list: list[str] = [
            "sounds/background1.wav",
            "sounds/background2.ogg",
        ]
        background: str = choice(background_list)

        pygame.mixer.music.load(background)
        pygame.mixer.music.set_volume(0.4)
