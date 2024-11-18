#!/usr/bin/env python3

"""
This module defines the 'Buttons' class to make and manage various buttons in the game.

It creates buttons, such as play, pause, menu, and difficulty.
It also handles the rendering of text on the buttons
and displays additional information like credits or hotkeys.
"""

from typing import TYPE_CHECKING
from pathlib import Path
import pygame.font

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Buttons:  # pylint: disable=R0902, R0913
    """A class to build buttons for the game."""

    def __init__(self, ai_game: "AlienInvasion", msg: str) -> None:
        """Initialize button attributes."""
        self.screen: pygame.Surface = ai_game.screen
        self.screen_rect: pygame.Rect = self.screen.get_rect()
        self.msg = msg

        # Initialize button properties
        self._set_button_properties()
        # Initialize additional attributes.
        self.msg_image: pygame.Surface = pygame.Surface((0, 0))
        self.msg_image_rect: pygame.Rect = self.msg_image.get_rect()
        self.artist_color: tuple[int, int, int] = (200, 100, 0)
        self.sound_color: tuple[int, int, int] = (0, 150, 150)
        self.image_color: tuple[int, int, int] = (0, 128, 0)
        self.keys: tuple[int, int, int] = (0, 128, 0)

    def _set_button_properties(
        self,
        width: int = 50,
        height: int = 20,
        font_size: int = 48,
        button_color: tuple[int, int, int] = (0, 0, 0),
        text_color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        """Set and initialize the dimensions and properties of the button."""
        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color
        self.font: pygame.font.Font = pygame.font.SysFont(None, font_size, bold=False, italic=True)
        self.rect: pygame.Rect = pygame.Rect(0, 0, self.width, self.height)

    def make_play_button(self) -> None:
        """Make the Play button."""
        self._set_button_properties(width=200, height=50, button_color=(230, 150, 0))
        # Center the object on the screen.
        self.rect.center = self.screen_rect.center
        # Render the message into an image.
        self._prep_msg()

    def make_pause_button(self) -> None:
        """Make the Pause button."""
        self._set_button_properties(font_size=20, button_color=(192, 31, 51))
        # Place the button on the top right of the screen.
        self.rect.right = self.screen_rect.right
        # Render the message into an image.
        self._prep_msg()

    def make_menu_button(self) -> None:
        """Make the Menu button."""
        self._set_button_properties(font_size=20, button_color=(125, 150, 0))
        # Place the button below the Pause button.
        self.rect.top = self.height
        self.rect.right = self.screen_rect.right
        # Render the message into an image.
        self._prep_msg()

    def make_difficulty_button(self) -> None:
        """Make the Difficulty button."""
        self._set_button_properties(font_size=14, button_color=(150, 175, 25))
        # Place the button below the Menu button.
        self.rect.top = self.height * 2
        self.rect.right = self.screen_rect.right
        # Render the message into an image.
        self._prep_msg()

    def make_easy_difficulty_button(self, highlighted: bool = False) -> None:
        """Make the Easy difficulty button."""
        # Highlight it only if the user clicks the button.
        color: tuple[int, int, int] = (50, 50, 50) if highlighted else (241, 195, 76)
        self._set_button_properties(width=200, height=50, button_color=color)

        # Center the object on the screen below the Play button.
        self.rect.top = (self.screen_rect.height // 2) + (self.rect.height // 2)
        self.rect.centerx = self.screen_rect.centerx
        # Render the message into an image.
        self._prep_msg()

    def make_medium_difficulty_button(self, highlighted: bool = False) -> None:
        """Make the Medium difficulty button."""
        # Highlight it only if the user clicks the button.
        color: tuple[int, int, int] = (50, 50, 50) if highlighted else (235, 172, 38)
        self._set_button_properties(width=200, height=50, button_color=color)

        # Center the object on the screen below the Easy button.
        self.rect.top = (self.screen_rect.height // 2) + (self.rect.height) + (self.rect.height // 2)
        self.rect.centerx = self.screen_rect.centerx
        # Render the message into an image.
        self._prep_msg()

    def make_hard_difficulty_button(self, highlighted: bool = False) -> None:
        """Make the Hard difficulty button."""
        # Highlight it only if the user clicks the button.
        color: tuple[int, int, int] = (50, 50, 50) if highlighted else (161, 105, 0)
        self._set_button_properties(width=200, height=50, button_color=color)

        # Center the object on the screen below the Medium button.
        self.rect.top = (self.screen_rect.height // 2) + (self.rect.height * 2) + (self.rect.height // 2)
        self.rect.centerx = self.screen_rect.centerx
        # Render the message into an image.
        self._prep_msg()

    def make_hotkeys_button(self) -> None:
        """Make the Hotkeys button."""
        self._set_button_properties(font_size=15, button_color=(110, 135, 0))
        # Place the button below the Difficulty button.
        self.rect.top = self.height * 3
        self.rect.right = self.screen_rect.right
        # Render the message into an image.
        self._prep_msg()

    def make_credits_button(self) -> None:
        """Make the Credits button."""
        self._set_button_properties(font_size=15, button_color=(70, 90, 0))
        # Place the button below the Hotkeys button.
        self.rect.top = self.height * 4
        self.rect.right = self.screen_rect.right
        # Render the message into an image.
        self._prep_msg()

    def make_credits_display_button(self, ai_game: "AlienInvasion", show_credits: bool = True) -> None:
        """Make a button and use it as a screen where to display the credits."""
        self._set_button_properties(
            width=ai_game.settings.screen_width,
            height=ai_game.settings.screen_height,
            font_size=0,
            button_color=(255, 255, 255),
            text_color=(0, 0, 0),
        )

        # Place the button at the center of the screen.
        self.rect.center = self.screen_rect.center
        self._read_credits_or_hotkeys(show_credits)

    def _read_credits_or_hotkeys(self, show_credits: bool = True) -> None:
        """Read the content from credits.txt or hotkeys.txt and display it."""
        path: Path = Path("txt_files", "credits.txt") if show_credits else Path("txt_files", "hotkeys.txt")
        content: str = path.read_text(encoding="utf-8")
        lines: list[str] = content.splitlines()
        self._render_credits_or_hotkeys(lines, show_credits)

    def _render_credits_or_hotkeys(self, lines: list[str], show_credits: bool) -> None:
        """Render the credits or hotkeys on the button surface."""
        if show_credits:
            font: pygame.font.Font = pygame.font.SysFont("Tahoma", 9, bold=True)
            colored_lines: list[tuple[str, tuple[int, int, int]]] = self._colorize_credits_lines(lines)
        elif not show_credits:
            font = pygame.font.SysFont("DejaVu Sans", 15, bold=True)
            colored_lines = self._colorize_hotkeys_lines(lines)

        surface: pygame.Surface = self._make_surface(font, colored_lines)
        self._prep_credits_or_hotkeys(surface)

    def _colorize_credits_lines(self, lines: list[str]) -> list[tuple[str, tuple[int, int, int]]]:
        """Colorize the credits' lines based on keywords."""
        colored_lines: list[tuple[str, tuple[int, int, int]]] = []

        for line in lines:
            if "artist" in line.lower():
                color: tuple[int, int, int] = self.artist_color
            elif "sound" in line.lower():
                color = self.sound_color
            elif "image" in line.lower():
                color = self.image_color
            else:
                color = self.text_color
            colored_lines.append((line, color))

        return colored_lines

    def _colorize_hotkeys_lines(self, lines: list[str]) -> list[tuple[str, tuple[int, int, int]]]:
        """Colorize the hotkeys' lines based on keywords."""
        colored_lines: list[tuple[str, tuple[int, int, int]]] = [
            (line, self.keys if " keys" in line.lower() else self.text_color) for line in lines
        ]

        return colored_lines

    def _make_surface(
        self,
        font: pygame.font.Font,
        colored_lines: list[tuple[str, tuple[int, int, int]]],
    ) -> pygame.Surface:
        """Create a surface to hold the rendered lines."""
        max_line_width: int = 0
        total_height: int = 0
        rendered_lines: list[pygame.Surface] = []

        # Render each line.
        for line, color in colored_lines:
            rendered_line: pygame.Surface = font.render(line, True, color, self.button_color)
            rendered_lines.append(rendered_line)

        for rendered_line in rendered_lines:
            total_height += rendered_line.get_height()
            max_line_width = max(max_line_width, rendered_line.get_width())

        # Create a surface to hold all the rendered lines.
        surface: pygame.Surface = pygame.Surface(
            (max_line_width, total_height), pygame.SRCALPHA  # pylint: disable=E1101
        )

        # Blit each line onto the surface.
        y: int = 0
        for rendered_line in rendered_lines:
            surface.blit(rendered_line, (0, y))
            y += rendered_line.get_height()

        return surface

    def _prep_credits_or_hotkeys(self, surface: pygame.Surface) -> None:
        """Turn the credits or hotkeys into a rendered image."""
        self.msg_image = surface
        self.msg_image_rect = surface.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _prep_msg(self) -> None:
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        """Draw blank buttons and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
