#!/usr/bin/env python3

"""
This module defines the 'HungryFox' class that manages the core functionality
of the Hungry Fox game.

Key Features:
- Initializes game settings, screen, and resources.
- Manages game states such as starting, pausing, and restarting.
- Controls game difficulty.
- Handles user input including keyboard and mouse events.
- Updates and render game objects including the fox, bullets, and farmer enemies.
- Manages game UI elements such as buttons and scoreboards.
"""

from __future__ import annotations
import sys
from random import random
from time import sleep, time
import json
from pathlib import Path

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from buttons import Buttons
from fox import Fox
from bullet import Bullet
from farmer import Farmer
from farmer_bullet import FarmerBullet
from sound_effects import Sound


class GameState:  # pylint: disable = R0902, R0903
    """A class to store all game-state related attributes."""

    def __init__(self) -> None:
        """Initialize game state attributes."""
        self.game_active: bool = False
        self.game_paused: bool = False
        self.sub_menu: bool = False
        self.difficulty_levels: bool = False
        self.game_restarted: bool = False
        self.show_credits: bool = False
        self.show_hotkeys: bool = False
        self.mouse_visible: bool = False
        self.last_mouse_movement: float = 0.0


class GameButtons:  # pylint: disable=R0902
    """A class to store all the buttons used in the game."""

    def __init__(self, h_fox: HungryFox) -> None:
        """Initialize all game buttons."""
        self.initialize_starting_game_buttons(h_fox)
        self.initialize_other_game_buttons(h_fox)

    def initialize_starting_game_buttons(self, h_fox: HungryFox) -> None:
        """Initialize buttons that are visible when the game starts."""
        self.play_button: Buttons = Buttons(h_fox, "Play")
        self.play_button.make_play_button()

        self.pause_button: Buttons = Buttons(h_fox, "Pause")
        self.pause_button.make_pause_button()

        self.menu_button: Buttons = Buttons(h_fox, "Menu")
        self.menu_button.make_menu_button()

    def initialize_other_game_buttons(self, h_fox: HungryFox) -> None:
        """Initialize all the buttons that are not visible when the game starts."""
        self.resume_button: Buttons = Buttons(h_fox, "Resume")
        self.restart_button: Buttons = Buttons(h_fox, "Restart")
        self.difficulty_button: Buttons = Buttons(h_fox, "Difficulty")
        self.easy_diff_button: Buttons = Buttons(h_fox, "Easy")
        self.medium_diff_button: Buttons = Buttons(h_fox, "Medium")
        self.hard_diff_button: Buttons = Buttons(h_fox, "Hard")
        self.hotkeys_button: Buttons = Buttons(h_fox, "Hotkeys")
        self.credits_button: Buttons = Buttons(h_fox, "Credits")
        self.credits_display_button: Buttons = Buttons(h_fox, "")
        self.hotkeys_display_button: Buttons = Buttons(h_fox, "")
        self.exit_button: Buttons = Buttons(h_fox, "Exit")


class HungryFox:  # pylint: disable = R0902, R0903
    """Class to manage the game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and generate game resources."""
        self.game_state: GameState = GameState()
        pygame.init()  # pylint: disable=E1101
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.settings: Settings = Settings()
        self.sounds: Sound = Sound()
        self._make_screen()
        self.stats: GameStats = GameStats(self)
        self.game_buttons: GameButtons = GameButtons(self)
        self.sb: Scoreboard = Scoreboard(self)
        self.fox: Fox = Fox(self)
        self._sprite_groups()
        self._make_fleet()

        # Counter to control the timing of fleet generation.
        # It prevents the fleet from being regenerated immediately
        #   after the first time the game starts.
        # The fleet will only be generated again if the fox is killed
        #   or in a new game run.
        self.fleet_generation: int = 0
        self.fleet_generation_limit: int = 1

    def _make_screen(self) -> None:
        """Generate the screen for the game."""
        self.screen: pygame.Surface = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Hungry Fox")

    def _sprite_groups(self) -> None:
        """Store the sprite groups of the game."""
        self.bullets: pygame.sprite.Group = pygame.sprite.Group()
        self.farmers: pygame.sprite.Group = pygame.sprite.Group()
        self.farmer_bullets: pygame.sprite.Group = pygame.sprite.Group()

    def run_game(self) -> None:
        """Main loop for the game."""
        while True:
            self._check_events()

            if (self.game_state.game_active) and (not self.game_state.game_paused):
                self._make_mouse_invisible()
                self.fox.update()
                self._update_bullets()
                self._update_farmers()
                self._fire_farmer_bullet()
                self._update_farmer_bullets()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=E1101
                self._save_high_score_and_exit()
            elif event.type == pygame.KEYDOWN:  # pylint: disable=E1101
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # pylint: disable=E1101
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=E1101
                self._check_mouse_button_down()
            elif event.type == pygame.MOUSEMOTION:  # pylint: disable=E1101
                self._make_mouse_visible()

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        """Repond to keypresses."""
        if event.key == pygame.K_ESCAPE:  # pylint: disable=E1101
            self._save_high_score_and_exit()
        else:
            self._check_keydown_fox_events(event)
            self._check_keydown_buttons_events(event)

    def _check_keydown_fox_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses linked to the fox."""
        if event.key == pygame.K_RIGHT:  # pylint: disable=E1101
            self.fox.moving_right = True
        elif event.key == pygame.K_LEFT:  # pylint: disable=E1101
            self.fox.moving_left = True
        elif event.key == pygame.K_SPACE:  # pylint: disable=E1101
            self._fire_bullet()

    def _check_keydown_buttons_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses of buttons."""
        # Make sub-menu buttons if Menu is clicked.
        if (event.key == pygame.K_m) and (self._is_game_inactive_or_paused()):  # pylint: disable=E1101
            self._make_sub_menu_buttons()
        else:
            # Respond to keypresses of game state or sub-menu buttons.
            self._check_keydown_game_states_events(event)
            self._check_keydown_sub_menu_buttons_events(event)

    def _check_keydown_game_states_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses of buttons related to the game state."""
        if not self.game_state.game_active:
            self._check_keydown_start_game_events(event)
        elif self.game_state.game_active:
            self._check_keydown_running_game_events(event)
            self._check_keydown_paused_game_events(event)

    def _check_keydown_start_game_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses when the game is not active."""
        if self._is_return_key_and_no_credits_or_hotkeys(event):
            self.fleet_generation += self.fleet_generation_limit
            self._start_game()

    def _check_keydown_running_game_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses when the game is active and running."""
        if event.key == pygame.K_p:  # pylint: disable=E1101
            self._pause_game()

    def _check_keydown_paused_game_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses when the game is active but paused."""
        if self._is_return_key_and_no_credits_or_hotkeys(event) and (not self.game_state.game_restarted):
            self._unpause_game()
        elif self._is_return_key_and_no_credits_or_hotkeys(event) and (self.game_state.game_restarted):
            self._restart_game()

    def _is_return_key_and_no_credits_or_hotkeys(self, event: pygame.event.Event) -> bool:
        """
        Check if the Return key is pressed
        and neither credits nor hotkeys are displayed.
        """
        return (event.key == pygame.K_RETURN) and (  # pylint: disable=E1101
            self._are_credits_and_hotkeys_not_displayed()
        )

    def _check_keydown_sub_menu_buttons_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses of the sub-menu buttons."""
        # Respond if the sub-menu buttons are called via keypresses.
        if self.game_state.sub_menu:
            if event.key == pygame.K_d:
                self._make_sub_menu_buttons()
                self._make_difficulty_levels_buttons()
            elif (event.key == pygame.K_k) and (not self.game_state.show_credits):
                self._make_hotkeys_display()
            elif (event.key == pygame.K_c) and (not self.game_state.show_hotkeys):
                self._make_credits_display()
        if (event.key == pygame.K_e) and (self._are_credits_or_hotkeys_shown()):  # pylint: disable=E1101
            self._exit_credits_or_hotkeys()
        else:
            # Respond to the keypresses to choose the game difficulty.
            self._check_keydown_start_difficulty_buttons(event)
            self._check_keydown_restart_difficulty_buttons(event)

    def _check_keydown_start_difficulty_buttons(self, event: pygame.event.Event) -> None:
        """Respond to keypresses of the start-game difficulty buttons."""
        if (self._can_choose_difficulty()) and (self._are_credits_and_hotkeys_not_displayed()):
            if event.key == pygame.K_1:
                self._easy_difficulty()
            elif event.key == pygame.K_2:
                self._medium_difficulty()
            elif event.key == pygame.K_3:
                self._hard_difficulty()

    def _check_keydown_restart_difficulty_buttons(self, event: pygame.event.Event) -> None:
        """Respond to keypresses of the restart-game difficulty buttons."""
        if self._can_restart_game() and (self._are_credits_and_hotkeys_not_displayed()):
            if event.key == pygame.K_1:
                self._easy_difficulty()
                self._make_restart_button()
            elif event.key == pygame.K_2:
                self._medium_difficulty()
                self._make_restart_button()
            elif event.key == pygame.K_3:
                self._hard_difficulty()
                self._make_restart_button()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:  # pylint: disable=E1101
            self.fox.moving_right = False
        elif event.key == pygame.K_LEFT:  # pylint: disable=E1101
            self.fox.moving_left = False

    def _check_mouse_button_down(self) -> None:
        """Respond to mouse clicks of various buttons."""
        self._check_mouse_button_down_play_button()
        self._check_mouse_button_down_pause_button()
        self._check_mouse_button_down_resume_button()
        self._check_mouse_button_down_menu_button()
        self._check_mouse_button_down_difficulty_button()
        self._check_mouse_button_down_difficulty_levels_buttons()
        self._check_mouse_button_down_credits_button()
        self._check_mouse_button_down_hotkeys_button()
        self._check_mouse_button_down_exit_button()
        if hasattr(self.game_buttons, "restart_button"):
            self._check_mouse_button_down_restart_button()

    def _is_button_clicked(self, button: Buttons) -> bool:
        """Check if a button is clicked."""
        return button.rect.collidepoint(pygame.mouse.get_pos())

    def _check_mouse_button_down_play_button(self) -> None:
        """Start a new game if the Play button is clicked."""
        play_clicked: bool = self._is_button_clicked(self.game_buttons.play_button)
        if (play_clicked) and (not self.game_state.game_active) and (self._are_credits_and_hotkeys_not_displayed()):
            self.fleet_generation += self.fleet_generation_limit
            self._start_game()

    def _start_game(self) -> None:
        """Start a new game."""
        # Reset the game statistics, settings and stop the end_game sound.
        self.sounds.end_game.stop()
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self._prep_starting_scoreboard()

        # Set initial game flags.
        self._start_game_flags()

        # Play the background music.
        self.sounds.background_music()
        pygame.mixer.music.play(-1)

        # Get rid of any bullets and farmers and make a new fleet
        #   but only if the play button has been clicked more than once.
        if (self.fleet_generation > self.fleet_generation_limit) or (self.game_state.game_restarted):
            self._empty_sprites()
            self._make_fleet()

        self.fox.center_fox()

    def _prep_starting_scoreboard(self) -> None:
        """Make the score, level and fox images for the Scoreboard."""
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_foxes()

    def _start_game_flags(self) -> None:
        """Store the flags used at the start of the game."""
        self.game_state.game_active = True
        self.game_state.sub_menu = False
        self.game_state.difficulty_levels = False

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _empty_sprites(self) -> None:
        """Empty the sprite groups."""
        self.bullets.empty()
        self.farmer_bullets.empty()
        self.farmers.empty()

    def _check_mouse_button_down_pause_button(self) -> None:
        """Pause the game if the Pause button is clicked."""
        pause_clicked: bool = self._is_button_clicked(self.game_buttons.pause_button)
        if (pause_clicked) and (self.game_state.game_active):
            self._pause_game()

    def _pause_game(self) -> None:
        """Pause the game and generate a Resume button."""
        self.game_state.game_paused = True

        # The Resume button goes in the same place as the Play button.
        self.game_buttons.resume_button.make_play_button()

        # Stop or pause the music not only the game.
        self.sounds.farmer_death.stop()
        self.sounds.fox_fire.stop()
        pygame.mixer.music.pause()

        # Make mouse cursor visible.
        pygame.mouse.set_visible(True)

    def _check_mouse_button_down_resume_button(self) -> None:
        """Unpause the game if the Resume button is clicked."""
        if hasattr(self.game_buttons, "resume_button"):
            resume_clicked: bool = self._is_button_clicked(self.game_buttons.resume_button)
            if (
                (resume_clicked)
                and (self.game_state.game_paused)
                and (not self.game_state.game_restarted)
                and (self._are_credits_and_hotkeys_not_displayed())
            ):
                self._unpause_game()

    def _unpause_game(self) -> None:
        """Unpause the game."""
        self.game_state.game_paused = False
        pygame.mouse.set_visible(False)

        # Hide the sub_menu buttons.
        self.game_state.sub_menu = False
        # Hide the difficulty levels buttons.
        self.game_state.difficulty_levels = False

        # Unpause the music not only the game.
        pygame.mixer.music.unpause()

    def _check_mouse_button_down_menu_button(self) -> None:
        """Generate sub-menu buttons if Menu is clicked."""
        menu_clicked: bool = self._is_button_clicked(self.game_buttons.menu_button)
        if (menu_clicked) and self._is_game_inactive_or_paused():
            self._make_sub_menu_buttons()

    def _is_game_inactive_or_paused(self) -> bool:
        """Check if the game is inactive or paused."""
        return not self.game_state.game_active or self.game_state.game_paused

    def _make_sub_menu_buttons(self) -> None:
        """Make the Difficulty, Hotkeys and Credits buttons."""
        self.game_buttons.difficulty_button.make_difficulty_button()
        self.game_buttons.hotkeys_button.make_hotkeys_button()
        self.game_buttons.credits_button.make_credits_button()

        # Show the sub_menu buttons.
        self.game_state.sub_menu = True

    def _check_mouse_button_down_credits_button(self) -> None:
        """Generate the credits if the Credits button is clicked."""
        if self.game_state.sub_menu:
            credits_clicked: bool = self._is_button_clicked(self.game_buttons.credits_button)
            if credits_clicked:
                self._make_credits_display()

    def _make_credits_display(self) -> None:
        """Generate the credits and an Exit button."""
        # Consider the credits as if they were a button so they can be
        #   show on the screen.
        self.game_buttons.credits_display_button.make_credits_display_button(self)
        self._make_exit_button()

        self.game_state.show_credits = True

    def _make_exit_button(self) -> None:
        """Make the exit button for the credits and hotkeys."""
        self.game_buttons.exit_button.make_pause_button()

    def _check_mouse_button_down_hotkeys_button(self) -> None:
        """Generate the hotkeys if the Hotkeys button is clicked."""
        if self.game_state.sub_menu:
            hotkeys_clicked: bool = self._is_button_clicked(self.game_buttons.hotkeys_button)
            if (hotkeys_clicked) and (self._are_credits_and_hotkeys_not_displayed()):
                self._make_hotkeys_display()

    def _make_hotkeys_display(self) -> None:
        """Generate the hotkeys and an Exit button."""
        # Consider the hotkeys as if they were a button so they can be
        #   show on the screen.
        # Make the hotkeys button just like the credits button.
        self.game_buttons.hotkeys_display_button.make_credits_display_button(self, show_credits=False)
        self._make_exit_button()

        self.game_state.show_hotkeys = True

    def _check_mouse_button_down_exit_button(self) -> None:
        """Exit the credits or hotkeys if the Exit button is clicked."""
        if self._are_credits_or_hotkeys_shown():
            exit_clicked: bool = self._is_button_clicked(self.game_buttons.exit_button)
            if exit_clicked:
                self._exit_credits_or_hotkeys()

    def _exit_credits_or_hotkeys(self) -> None:
        """Deactivate the hotkeys and credits flags to exit."""
        self.game_state.show_credits = False
        self.game_state.show_hotkeys = False

    def _are_credits_or_hotkeys_shown(self) -> bool:
        """Check if the credits or hotkeys are displayed."""
        return (self.game_state.show_credits) or (self.game_state.show_hotkeys)

    def _are_credits_and_hotkeys_not_displayed(self) -> bool:
        """Check if the credits and hotkeys are not displayed."""
        return (not self.game_state.show_credits) and (not self.game_state.show_hotkeys)

    def _check_mouse_button_down_difficulty_button(self) -> None:
        """Generate the difficulty levels buttons if Difficulty is clicked."""
        if self.game_state.sub_menu:
            difficulty_clicked: bool = self._is_button_clicked(self.game_buttons.difficulty_button)
            if (difficulty_clicked) and (self._are_credits_and_hotkeys_not_displayed()):
                self._make_difficulty_levels_buttons()

    def _make_difficulty_levels_buttons(self) -> None:
        """Make the difficulty levels buttons."""
        self.game_buttons.easy_diff_button.make_easy_difficulty_button()
        self.game_buttons.medium_diff_button.make_medium_difficulty_button()
        self.game_buttons.hard_diff_button.make_hard_difficulty_button()

        # Show the difficulty levels buttons.
        self.game_state.difficulty_levels = True

    def _check_mouse_button_down_difficulty_levels_buttons(self) -> None:
        """Respond when the difficulty level buttons are clicked."""
        if self._can_choose_difficulty():
            easy_clicked, medium_clicked, hard_clicked = self._choose_difficulty()

            # Select the difficulty at the start of the game.
            self._handle_difficulty_selection(easy_clicked, medium_clicked, hard_clicked)
        else:
            # Change difficulty mid game.
            self._change_difficulty()

    def _can_choose_difficulty(self) -> bool:
        """Check if the difficulty can be change."""
        return (self.game_state.difficulty_levels) and (not self.game_state.game_paused)

    def _change_difficulty(self) -> None:
        """Allow the player to change the difficulty mid game."""
        if self._can_restart_game():
            easy_clicked, medium_clicked, hard_clicked = self._choose_difficulty()

            # Select a new difficulty if game paused; restart the game.
            self._handle_difficulty_selection(easy_clicked, medium_clicked, hard_clicked)
            self._check_and_make_restart_button(easy_clicked, medium_clicked, hard_clicked)

    def _can_restart_game(self) -> bool:
        """Check if game can be restarted."""
        return (self.game_state.difficulty_levels) and (self.game_state.game_paused)

    def _choose_difficulty(self) -> tuple[bool, bool, bool]:
        """Store attributes for the click of the difficulty levels buttons."""
        easy_clicked: bool = self._is_button_clicked(self.game_buttons.easy_diff_button)
        medium_clicked: bool = self._is_button_clicked(self.game_buttons.medium_diff_button)
        hard_clicked: bool = self._is_button_clicked(self.game_buttons.hard_diff_button)

        return easy_clicked, medium_clicked, hard_clicked

    def _check_and_make_restart_button(self, easy_clicked: bool, medium_clicked: bool, hard_clicked: bool) -> None:
        """Check conditions and generate the Restart button."""
        if (easy_clicked) or (medium_clicked) or (hard_clicked):
            self._make_restart_button()

    def _make_restart_button(self) -> None:
        """Make the Restart button."""
        # The Restart button goes where was the Play button.
        self.game_buttons.restart_button.make_play_button()
        self.game_state.game_restarted = True

    def _check_mouse_button_down_restart_button(self) -> None:
        """Restart the game if the Restart button is clicked."""
        restart_clicked: bool = self._is_button_clicked(self.game_buttons.restart_button)
        if (restart_clicked) and (self.game_state.game_restarted) and (self._are_credits_and_hotkeys_not_displayed()):
            self._restart_game()

    def _restart_game(self) -> None:
        """Restart the game."""
        self.game_state.game_paused = False
        self._start_game()
        self.game_state.game_restarted = False

    def _handle_difficulty_selection(self, easy_clicked: bool, medium_clicked: bool, hard_clicked: bool) -> None:
        """Handle the difficulty selection based on which button is clicked."""
        if self._are_credits_and_hotkeys_not_displayed():
            if easy_clicked:
                self._easy_difficulty()
            elif medium_clicked:
                self._medium_difficulty()
            elif hard_clicked:
                self._hard_difficulty()

    def _easy_difficulty(self) -> None:
        """Easy difficulty configurations."""
        self._set_difficulty(easy=True)

    def _medium_difficulty(self) -> None:
        """Medium difficulty configurations."""
        self._set_difficulty(medium=True)

    def _hard_difficulty(self) -> None:
        """Hard difficulty configurations."""
        self._set_difficulty(hard=True)

    def _set_difficulty(self, easy: bool = False, medium: bool = False, hard: bool = False) -> None:
        """Set difficulty configurations."""
        self._set_highlight_difficulty_levels_buttons(easy, medium, hard)
        self._choose_difficulty_settings(easy, medium, hard)

    def _set_highlight_difficulty_levels_buttons(self, easy: bool, medium: bool, hard: bool) -> None:
        """Define which of the difficulty levels buttons to highlight."""
        self.game_buttons.easy_diff_button.make_easy_difficulty_button(easy)
        self.game_buttons.medium_diff_button.make_medium_difficulty_button(medium)
        self.game_buttons.hard_diff_button.make_hard_difficulty_button(hard)

    def _choose_difficulty_settings(self, easy: bool, medium: bool, hard: bool) -> None:
        """Select the difficulty settings of the game."""
        self.settings.difficulty_settings.easy_settings = easy
        self.settings.difficulty_settings.medium_settings = medium
        self.settings.difficulty_settings.hard_settings = hard

    def _make_mouse_visible(self) -> None:
        """Make the mouse cursor visible if the mouse is moved."""
        self.game_state.mouse_visible = True
        pygame.mouse.set_visible(self.game_state.mouse_visible)

        # Get the time for the movements of the mouse.
        self.game_state.last_mouse_movement = time()

    def _make_mouse_invisible(self) -> None:
        """Make the mouse cursor disappear after 2 seconds of inactivity."""
        mouse_inactivity_time: int = 2
        if hasattr(self.game_state, "mouse_visible"):
            current_time: float = time()
            if current_time - self.game_state.last_mouse_movement > mouse_inactivity_time:
                self.game_state.mouse_visible = False
                pygame.mouse.set_visible(self.game_state.mouse_visible)

    def _make_fleet(self) -> None:
        """Make the farmer's fleet."""
        # Fill the screen with the fleet until there is no room left.
        # Spacing between farmers is one farmer_width and one farmer_height/2.
        farmer: Farmer = Farmer(self)
        farmer_width: int
        farmer_height: int
        farmer_width, farmer_height = farmer.rect.size

        current_x: int = farmer_width
        current_y: int = farmer_height // 2
        while current_y < (self.settings.screen_height - (3 * farmer_height)):
            while current_x < (self.settings.screen_width - (2 * farmer_width)):
                self._make_farmer(current_x, current_y)
                current_x += 2 * farmer_width

            # Reset the x value once the row is full and increment the y value.
            current_x = farmer_width
            current_y += int(2 * farmer_height / 1.5)

    def _make_farmer(self, x_position: int, y_position: int) -> None:
        """Add a new farmer to the fleet."""
        new_farmer: Farmer = Farmer(self)
        new_farmer.x = x_position
        new_farmer.rect.x = x_position
        new_farmer.rect.y = y_position
        self.farmers.add(new_farmer)

    def _check_fleet_edges(self) -> None:
        """Respond appropriately if any farmers have reached an edge."""
        for farmer in self.farmers.sprites():
            if farmer.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Drop the entire fleet and change the fleet's direction."""
        for farmer in self.farmers.sprites():
            farmer.rect.y += self.settings.farmer_drop_speed
        self.settings.farmer_direction *= -1

    def _update_farmers(self) -> None:
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.farmers.update()

        # Check for farmer-fox collision and respond accordingly.
        self._check_farmer_fox_collisions()
        # Check for farmers that reached thhe bottom of the screen.
        self._check_farmers_bottom()

        # Level up if all the farmers are shot down.
        self._level_up()

    def _check_farmer_fox_collisions(self) -> None:
        """Check for collisions between farmers and the fox."""
        if pygame.sprite.spritecollideany(self.fox, self.farmers):
            self._fox_hit()

    def _check_farmers_bottom(self) -> None:
        """Check if any farmers have reached the bottom of the screen."""
        for farmer in self.farmers.sprites():
            if farmer.rect.bottom >= self.screen.get_rect().bottom:
                # Treat this the same as if the fox got hit.
                self._fox_hit()
                break

    def _level_up(self) -> None:
        """Destroy bullets, make a new fleet and increase difficulty."""
        if not self.farmers:
            self._empty_sprites()
            self._make_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _fox_hit(self) -> None:
        """Respond to the fox being hit by a farmer or a bullet."""
        if self.stats.fox_life > 0:
            # Decrement fox_left, and update scoreboard.
            self.stats.fox_life -= 1
            self.sb.prep_foxes()

            # Get rid of any remaining bullets and farmers.
            self._empty_sprites()

            self._make_fleet()
            self.fox.center_fox()

            # Pause the game.
            sleep(0.5)
        else:
            self.game_state.game_active = False
            self._make_difficulty_levels_buttons()
            self._stop_music()
            self.sounds.end_game.play()
            pygame.mouse.set_visible(True)

    def _fire_bullet(self) -> None:
        """Make a new bullet and add it to the bullets group."""
        if (self.game_state.game_active) and (not self.game_state.game_paused):
            if len(self.bullets) < self.settings.difficulty_settings.bullets_allowed:
                new_bullet: Bullet = Bullet(self)
                self.bullets.add(new_bullet)

                # Play a sound when firing.
                self.sounds.fox_fire.play()

    def _update_bullets(self) -> None:
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of old bullets when they disappear from the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for bullet-farmer collisions and respond.
        self._check_bullet_farmer_collisions()

    def _check_bullet_farmer_collisions(self) -> None:
        """Respond to collisions between bullets and farmers."""
        collisions: dict[pygame.sprite.Sprite, list[pygame.sprite.Sprite]] = pygame.sprite.groupcollide(
            self.bullets, self.farmers, True, True
        )

        # Play a sound when a farmer is hit.
        self._farmer_hit_sound(collisions)
        # Increment the score if there is a collision.
        self._increment_score(collisions)

    def _increment_score(self, collisions: dict[pygame.sprite.Sprite, list[pygame.sprite.Sprite]]) -> None:
        """Increment the score when farmers are hit."""
        if collisions:
            for farmers in collisions.values():
                self.stats.score += self.settings.difficulty_settings.farmer_points * len(farmers)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _farmer_hit_sound(self, collisions: dict[pygame.sprite.Sprite, list[pygame.sprite.Sprite]]) -> None:
        """Play a sound when a farmer is hit by a bullet."""
        if collisions:
            self.sounds.farmer_death.play()

    def _make_farmer_bullet(self) -> None:
        """Make a new farmer's bullet and add it to the farmer_bullets group."""
        if len(self.farmer_bullets) < self.settings.difficulty_settings.farmer_bullets_allowed:
            new_farmer_bullet: FarmerBullet = FarmerBullet(self)
            self.farmer_bullets.add(new_farmer_bullet)

    def _check_farmers(self) -> None:
        """Check if farmers are added to the group and make farmer's bullets."""
        if self.farmers:
            self._make_farmer_bullet()

    def _fire_farmer_bullet(self) -> None:
        """Fire the farmers' bullets at random intervals."""
        if random() < self.settings.shooting_frequency:
            self._check_farmers()

    def _update_farmer_bullets(self) -> None:
        """Update farmers' bullets position and get rid of their old bullets."""
        self.farmer_bullets.update()

        # Get rid of old farmers' bullets.
        for farmer_bullet in self.farmer_bullets.copy():
            if farmer_bullet.rect.top >= self.screen.get_rect().bottom:
                self.farmer_bullets.remove(farmer_bullet)

        # Check for farmers' bullets and fox collisions and respond.
        self._check_farmer_bullet_fox_collisions()

    def _check_farmer_bullet_fox_collisions(self) -> None:
        """Respond to collisions between farmers' bullets and the fox."""
        if pygame.sprite.spritecollideany(self.fox, self.farmer_bullets):
            self._fox_hit()

    def _stop_music(self) -> None:
        """Stop all music if the fox has no lives left."""
        pygame.mixer.music.stop()
        self.sounds.fox_fire.stop()
        self.sounds.farmer_death.stop()

    def _draw_fox_objects(self) -> None:
        """Draw fox related objects."""
        self.bullets.draw(self.screen)
        self.fox.blitme()

    def _draw_farmer_objects(self) -> None:
        """Draw farmer related objects."""
        self.farmer_bullets.draw(self.screen)
        self.farmers.draw(self.screen)

    def _draw_buttons(self) -> None:
        """Draw the buttons for the game based on the current state."""
        self._draw_game_state_buttons()
        self._draw_menu_buttons()

    def _draw_game_state_buttons(self) -> None:
        """Draw the game state buttons."""
        if not self.game_state.game_active:
            self.game_buttons.play_button.draw_button()

        if not self.game_state.game_paused:
            self.game_buttons.pause_button.draw_button()

        if (self.game_state.game_paused) and (not self.game_state.game_restarted):
            self.game_buttons.resume_button.draw_button()

        if (self.game_state.game_paused) and (self.game_state.game_restarted):
            self.game_buttons.restart_button.draw_button()

        if self._are_credits_and_hotkeys_not_displayed():
            self.sb.show_score()

    def _draw_menu_buttons(self) -> None:
        """Draw the buttons related to the menu."""
        if (not self.game_state.game_active) or (self.game_state.game_paused):
            self.game_buttons.menu_button.draw_button()

        if self.game_state.sub_menu:
            self.game_buttons.difficulty_button.draw_button()
            self.game_buttons.hotkeys_button.draw_button()
            self.game_buttons.credits_button.draw_button()

        if self.game_state.show_credits:
            self.game_buttons.credits_display_button.draw_button()
            self.game_buttons.exit_button.draw_button()

        if self.game_state.show_hotkeys:
            self.game_buttons.hotkeys_display_button.draw_button()
            self.game_buttons.exit_button.draw_button()

        if (self.game_state.difficulty_levels) and (self._are_credits_and_hotkeys_not_displayed()):
            self.game_buttons.easy_diff_button.draw_button()
            self.game_buttons.medium_diff_button.draw_button()
            self.game_buttons.hard_diff_button.draw_button()

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.settings.background, (0, 0))
        self._draw_fox_objects()
        self._draw_farmer_objects()
        self._draw_buttons()

        pygame.display.flip()

    def _save_high_score_and_exit(self) -> None:
        """Save the high score when the user quits the game and exit."""
        saved_high_score: int = self.stats.read_high_score()
        if self.stats.high_score > saved_high_score:
            path: Path = Path("high_score", "high_score.json")
            high_score: str = json.dumps(self.stats.high_score)
            path.write_text(high_score, encoding="utf-8")

        sys.exit()


if __name__ == "__main__":
    # Generate the instance to run the game.
    hungry_fox = HungryFox()
    hungry_fox.run_game()
