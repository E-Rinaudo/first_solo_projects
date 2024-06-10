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


class HungryFox:
    """Class to manage the game and behavior."""

    def __init__(self):
        """Initialize the game, and generate game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.sounds = Sound()

        self._make_screen()

        self.stats = GameStats(self)

        self._initialize_starting_game_buttons()

        self.sb = Scoreboard(self)
        self.fox = Fox(self)

        self._sprite_groups()
        self._make_fleet()
        self._initialize_flags()
        
        # Counter to control the timing of fleet generation.
        # It prevents the fleet from being regenerated immediately 
        #   after the first time the game starts.
        # The fleet will only be generated again if the fox is killed 
        #   or in a new game run.
        self.fleet_generation = 0
        self.FLEET_GENERATION_LIMIT = 1
    
    def _make_screen(self):
        """Generate the screen for the game."""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Hungry Fox")

    def _sprite_groups(self):
        """Store the sprite groups of the game."""
        self.bullets = pygame.sprite.Group()
        self.farmers = pygame.sprite.Group()
        self.farmer_bullets = pygame.sprite.Group()
    
    def _initialize_flags(self):
        """Initialize game state flags."""
        self.game_active = False
        self.game_paused = False 
        self.sub_menu = False
        self.difficulty_levels = False
        self.game_restarted = False
        self.show_credits = False
        self.show_hotkeys = False
    
    def _initialize_starting_game_buttons(self):
        """Make buttons that are visible when the game starts."""   
        self.play_button = Buttons(self, "Play")
        self.play_button.make_play_button()

        self.pause_button = Buttons(self, "Pause")
        self.pause_button.make_pause_button()

        self.menu_button = Buttons(self, "Menu")
        self.menu_button.make_menu_button()

    def run_game(self):
        """Main loop for the game."""
        while True:
            self._check_events()

            if (self.game_active) and (not self.game_paused):
                self._make_mouse_invisible()
                self.fox.update()
                self._update_bullets()
                self._update_farmers()
                self._fire_farmer_bullet()
                self._update_farmer_bullets()
            
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._save_high_score_and_exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_button_down()
            elif event.type == pygame.MOUSEMOTION:
                self._make_mouse_visible()

    def _check_keydown_events(self, event):
        """Repond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            self._save_high_score_and_exit()
        else:
            self._check_keydown_fox_events(event)
            self._check_keydown_buttons_events(event)
        
    def _check_keydown_fox_events(self, event):
        """Respond to keypresses linked to the fox."""
        if event.key == pygame.K_RIGHT:
            self.fox.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.fox.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keydown_buttons_events(self, event):
        """Respond to keypresses of buttons."""
        # Make sub-menu buttons if Menu is clicked.
        if (event.key == pygame.K_m) and (self._is_game_inactive_or_paused()):
            self._make_sub_menu_buttons()
        else:
            # Respond to keypresses of game state or sub-menu buttons.    
            self._check_keydown_game_states_events(event)
            self._check_keydown_sub_menu_buttons_events(event)
    
    def _check_keydown_game_states_events(self, event):
        """Respond to keypresses of buttons related to the game state."""
        if not self.game_active:
            self._check_keydown_start_game_events(event)
        elif self.game_active:
                self._check_keydown_running_game_events(event)
                self._check_keydown_paused_game_events(event)

    def _check_keydown_start_game_events(self, event):
        """Respond to keypresses when the game is not active."""
        if self._is_return_key_and_no_credits_or_hotkeys(event):
            self.fleet_generation += self.FLEET_GENERATION_LIMIT
            self._start_game()

    def _check_keydown_running_game_events(self, event):
        """Respond to keypresses when the game is active and running."""
        if event.key == pygame.K_p:
            self._pause_game()

    def _check_keydown_paused_game_events(self, event):
        """Respond to keypresses when the game is active but paused."""
        if (
            self._is_return_key_and_no_credits_or_hotkeys(event) 
            and (not self.game_restarted)
        ):
            self._unpause_game()
        elif (
            self._is_return_key_and_no_credits_or_hotkeys(event)
            and (self.game_restarted) 
        ):
            self._restart_game()
    
    def _is_return_key_and_no_credits_or_hotkeys(self, event):
        """
        Check if the Return key is pressed 
        and neither credits nor hotkeys are displayed.
        """
        return (
            (event.key == pygame.K_RETURN) 
            and (self._are_credits_and_hotkeys_not_displayed())
        )

    def _check_keydown_sub_menu_buttons_events(self, event):
        """Respond to keypresses of the sub-menu buttons."""
        # Respond if the sub-menu buttons are called via keypresses.
        if self.sub_menu:
            if event.key == pygame.K_d:
                self._make_sub_menu_buttons()
                self._make_difficulty_levels_buttons()
            elif (event.key == pygame.K_k) and (not self.show_credits):
                self._make_hotkeys_display()
            elif (event.key == pygame.K_c) and (not self.show_hotkeys):
                self._make_credits_display()
        if (
            (event.key == pygame.K_e) 
            and (self._are_credits_or_hotkeys_shown())
        ):
            self._exit_credits_or_hotkeys()
        else:
            # Respond to the keypresses to choose the game difficulty.
            self._check_keydown_start_difficulty_buttons(event)
            self._check_keydown_restart_difficulty_buttons(event)
        
    def _check_keydown_start_difficulty_buttons(self, event):
        """Respond to keypresses of the start-game difficulty buttons."""
        if (
            (self._can_choose_difficulty()) 
            and (self._are_credits_and_hotkeys_not_displayed())
        ):
            if event.key == pygame.K_1:
                self._easy_difficulty()
            elif event.key == pygame.K_2:
                self._medium_difficulty()
            elif event.key == pygame.K_3:
                self._hard_difficulty()

    def _check_keydown_restart_difficulty_buttons(self, event):
        """Respond to keypresses of the restart-game difficulty buttons."""
        if (
            self._can_restart_game() 
            and (self._are_credits_and_hotkeys_not_displayed())
        ):
            if event.key == pygame.K_1:
                self._easy_difficulty()
                self._instantiate_restart_button()
            elif event.key == pygame.K_2:
                self._medium_difficulty()
                self._instantiate_restart_button()
            elif event.key == pygame.K_3:
                self._hard_difficulty()
                self._instantiate_restart_button()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.fox.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fox.moving_left = False
    
    def _check_mouse_button_down(self):
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
        if hasattr(self, 'restart_button'):
            self._check_mouse_button_down_restart_button()
    
    def _is_button_clicked(self, button):
        """Check if a button is clicked."""
        return button.rect.collidepoint(pygame.mouse.get_pos())

    def _check_mouse_button_down_play_button(self):
        """Start a new game if the Play button is clicked."""
        play_clicked = self._is_button_clicked(self.play_button)
        if (
            (play_clicked) and (not self.game_active) 
            and (self._are_credits_and_hotkeys_not_displayed())
        ):
            self.fleet_generation += self.FLEET_GENERATION_LIMIT
            self._start_game()
    
    def _start_game(self):
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
        if (
            (self.fleet_generation > self.FLEET_GENERATION_LIMIT) 
            or (self.game_restarted)
        ):
            self._empty_sprites()
            self._make_fleet()

        self.fox.center_fox()
    
    def _prep_starting_scoreboard(self):
        """Make the score, level and fox images for the Scoreboard."""
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_foxs()

    def _start_game_flags(self):
        """Store the flags used at the start of the game."""
        self.game_active = True
        self.sub_menu = False
        self.difficulty_levels = False

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
    
    def _empty_sprites(self):
        """Empty the sprite groups."""
        self.bullets.empty()
        self.farmer_bullets.empty()
        self.farmers.empty()
    
    def _check_mouse_button_down_pause_button(self):
        """Pause the game if the Pause button is clicked."""
        pause_clicked = self._is_button_clicked(self.pause_button)
        if (pause_clicked) and (self.game_active):
            self._pause_game()
    
    def _pause_game(self):
        """Pause the game and generate a Resume button."""
        self.game_paused = True
        self.resume_button = Buttons(self, "Resume")

        # The Resume button goes in the same place as the Play button. 
        self.resume_button.make_play_button()

        # Stop or pause the music not only the game.  
        self.sounds.farmer_death.stop()
        self.sounds.fox_fire.stop()       
        pygame.mixer.music.pause()

        # Make mouse cursor visible.
        pygame.mouse.set_visible(True)

    def _check_mouse_button_down_resume_button(self):
        """Unpause the game if the Resume button is clicked."""
        if hasattr(self, 'resume_button'):
            resume_clicked = self._is_button_clicked(self.resume_button)
            if (
                (resume_clicked) 
                and (self.game_paused) 
                and (not self.game_restarted)
                and (self._are_credits_and_hotkeys_not_displayed())               
            ):
                self._unpause_game()
    
    def _unpause_game(self):
        """Unpause the game."""           
        self.game_paused = False
        pygame.mouse.set_visible(False)

        # Hide the sub_menu buttons.
        self.sub_menu = False
        # Hide the difficulty levels buttons.
        self.difficulty_levels = False    

        # Unpause the music not only the game.
        pygame.mixer.music.unpause()
    
    def _check_mouse_button_down_menu_button(self):
        """Generate sub-menu buttons if Menu is clicked."""
        menu_clicked = self._is_button_clicked(self.menu_button)
        if (menu_clicked) and self._is_game_inactive_or_paused():
            self._make_sub_menu_buttons()
    
    def _is_game_inactive_or_paused(self):
        """Check if the game is inactive or paused."""
        return (not self.game_active or self.game_paused)
    
    def _make_sub_menu_buttons(self):
        """Make instances for the Difficulty, Hotkeys and Credits buttons."""
        self.difficulty_button = Buttons(self, "Difficulty")
        self.difficulty_button.make_difficulty_button()

        self.hotkeys_button = Buttons(self, "Hotkeys")
        self.hotkeys_button.make_hotkeys_button()

        self.credits_button = Buttons(self, "Credits")
        self.credits_button.make_credits_button()
        
        # Show the sub_menu buttons.
        self.sub_menu = True
    
    def _check_mouse_button_down_credits_button(self):
        """Generate the credits if the Credits button is clicked."""
        if self.sub_menu:
            self.credits_clicked = self._is_button_clicked(self.credits_button)
            if self.credits_clicked:
                self._make_credits_display()
    
    def _make_credits_display(self):
        """Generate the credits and an Exit button."""
        # Consider the credits as if they were a button so they can be
        #   show on the screen.
        self.credits_display_button = Buttons(self, None)
        self.credits_display_button.make_credits_display_button(self)

        self._make_exit_button()
    
        self.show_credits = True

    def _make_exit_button(self):
        """Make the exit button for the credits and hotkeys."""
        self.exit_button = Buttons(self, "Exit")
        self.exit_button.make_pause_button()

    def _check_mouse_button_down_hotkeys_button(self):
        """Generate the hotkeys if the Hotkeys button is clicked."""
        if self.sub_menu:
            self.hotkeys_clicked = self._is_button_clicked(self.hotkeys_button)
            if (
                (self.hotkeys_clicked) 
                and (self._are_credits_and_hotkeys_not_displayed())
            ):
                self._make_hotkeys_display()
    
    def _make_hotkeys_display(self):
        """Generate the hotkeys and an Exit button."""
        # Consider the hotkeys as if they were a button so they can be
        #   show on the screen.
        # Make the hotkeys button just like the credits button.
        self.hotkeys_display_button = Buttons(self, None)
        self.hotkeys_display_button.make_credits_display_button(self, 
                show_credits=False)

        self._make_exit_button()

        self.show_hotkeys = True

    def _check_mouse_button_down_exit_button(self):
        """Exit the credits or hotkeys if the Exit button is clicked."""
        if self._are_credits_or_hotkeys_shown():
            self.exit_clicked = self._is_button_clicked(self.exit_button)
            if self.exit_clicked:
                self._exit_credits_or_hotkeys()
    
    def _exit_credits_or_hotkeys(self):
        """Disactivate the hotkeys and credits flags to exit."""
        self.show_credits = False
        self.show_hotkeys = False
    
    def _are_credits_or_hotkeys_shown(self):
        """Check if the credits or hotkeys are displayed."""
        return (self.show_credits) or (self.show_hotkeys)
    
    def _are_credits_and_hotkeys_not_displayed(self):
        """Check if the credits and hotkeys are not displayed."""
        return (not self.show_credits) and (not self.show_hotkeys)
    
    def _check_mouse_button_down_difficulty_button(self):
        """Generate the difficulty levels buttons if Difficulty is clicked."""
        if self.sub_menu:
            difficulty_clicked = self._is_button_clicked(self.difficulty_button)
            if (
                (difficulty_clicked) 
                and (self._are_credits_and_hotkeys_not_displayed())
            ):
                self._make_difficulty_levels_buttons()
    
    def _make_difficulty_levels_buttons(self):
        """Make instances for the difficulty levels buttons."""
        self.easy_diff_button = Buttons(self, "Easy")    
        self.easy_diff_button.make_easy_difficulty_button()

        self.medium_diff_button = Buttons(self, "Medium")
        self.medium_diff_button.make_medium_difficulty_button()

        self.hard_diff_button = Buttons(self, "Hard")
        self.hard_diff_button.make_hard_difficulty_button()

        # Show the difficulty levels buttons.
        self.difficulty_levels = True
    
    def _check_mouse_button_down_difficulty_levels_buttons(self):
        """Respond when the difficulty level buttons are clicked."""
        if self._can_choose_difficulty():
            self._choose_difficulty()
            
            # Select the difficulty at the start of the game.
            self._handle_difficulty_selection()
        else:
            # Change difficulty mid game.
            self._change_difficulty()
    
    def _can_choose_difficulty(self):
        """Check if the difficulty can be change."""
        return (self.difficulty_levels) and (not self.game_paused)
    
    def _change_difficulty(self):
        """"Allow the player to change the difficulty mid game."""
        if self._can_restart_game():
            self._choose_difficulty()
            
            # Select a new difficulty if game paused; restart the game.
            self._handle_difficulty_selection()
            self._make_restart_button()
        
    def _can_restart_game(self):
        """Check if game can be restarted."""
        return (self.difficulty_levels) and (self.game_paused)
    
    def _choose_clicked(self):
        """Store attributes for the click of the difficulty levels buttons."""
        self.easy_clicked = self._is_button_clicked(self.easy_diff_button)
        self.medium_clicked = self._is_button_clicked(self.medium_diff_button)
        self.hard_clicked = self._is_button_clicked(self.hard_diff_button)
    
    def _make_restart_button(self):
        """Generate the Restart button."""
        if (self.easy_clicked) or (self.medium_clicked) or (self.hard_clicked):
            self._instantiate_restart_button()
    
    def _instantiate_restart_button(self):
        """Make the instance of the Restart button."""
        self.restart_button = Buttons(self, "Restart")

        # The Restart button goes where was the Play button. 
        self.restart_button.make_play_button()
        self.game_restarted = True
    
    def _check_mouse_button_down_restart_button(self):
        """Restart the game if the Restart button is clicked."""
        restart_clicked = self._is_button_clicked(self.restart_button)
        if (
            (restart_clicked) and (self.game_restarted) 
            and (self._are_credits_and_hotkeys_not_displayed())
        ):
            self._restart_game()
    
    def _restart_game(self):
        """Restart the game."""
        self.game_paused = False
        self._start_game()
        self.game_restarted = False
    
    def _handle_difficulty_selection(self):
        """Handle the difficulty selection based on which button is clicked."""
        if self._are_credits_and_hotkeys_not_displayed():
            if self.easy_clicked:
                self._easy_difficulty()
            elif self.medium_clicked:
                self._medium_difficulty()
            elif self.hard_clicked:
                self._hard_difficulty()
    
    def _easy_difficulty(self):
        """Easy difficulty configurations."""
        self._set_difficulty(easy=True)

    def _medium_difficulty(self):
        """Medium difficulty configurations."""
        self._set_difficulty(medium=True)

    def _hard_difficulty(self):
        """Hard difficulty configurations."""
        self._set_difficulty(hard=True)
    
    def _set_difficulty(self, easy=False, medium=False, hard=False):
        """Set difficulty configurations."""
        self._set_highlight_difficulty_levels_buttons(easy, medium, hard)
        self._choose_difficulty_settings(easy, medium, hard)
    
    def _set_highlight_difficulty_levels_buttons(self, easy, medium, hard):
        """Define which of the difficulty levels buttons to highlight."""
        self.easy_diff_button.make_easy_difficulty_button(easy)
        self.medium_diff_button.make_medium_difficulty_button(medium)
        self.hard_diff_button.make_hard_difficulty_button(hard)
    
    def _choose_difficulty_settings(self, easy, medium, hard):
        """Select the difficulty settings of the game."""
        self.settings.easy_settings = easy
        self.settings.medium_settings = medium
        self.settings.hard_settings = hard
            
    def _make_mouse_visible(self):
        """Make the mouse cursor visible if the mouse is moved."""
        self.mouse_visible = True
        pygame.mouse.set_visible(self.mouse_visible)

        # Get the time for the movements of the mouse.
        self.last_mouse_movement = time()

    def _make_mouse_invisible(self):
        """Make the mouse cursor disappear after 2 seconds of inactivity."""
        mouse_inactivity_time = 2
<<<<<<< HEAD
        if self.mouse_visible:
=======
        if hasattr(self, 'mouse_visible'):
>>>>>>> 317436f (Make the repository.)
            current_time = time()
            if current_time - self.last_mouse_movement > mouse_inactivity_time:
                self.mouse_visible = False
                pygame.mouse.set_visible(self.mouse_visible)

    def _make_fleet(self):
        """Make the farmer's fleet."""
        # Fill the screen with the fleet until there is no room left.
        # Spacing between farmers is one farmer_width and one farmer_height/2.
        farmer = Farmer(self)
        farmer_width, farmer_height = farmer.rect.size

        current_x, current_y = farmer_width, farmer_height/2
        while current_y < (self.settings.screen_height - (3 * farmer_height)):
            while current_x < (self.settings.screen_width - (2 * farmer_width)):
                self._make_farmer(current_x, current_y)
                current_x += 2 * farmer_width
            
            # Reset the x value once the row is full and increment the y value.
            current_x = farmer_width
            current_y += 2 * farmer_height/1.5
    
    def _make_farmer(self, x_position, y_position):
        """Add a new farmer to the fleet."""
        new_farmer = Farmer(self)
        new_farmer.x = x_position
        new_farmer.rect.x = x_position
        new_farmer.rect.y = y_position
        self.farmers.add(new_farmer)

    def _check_fleet_edges(self):
        """Respond appropriately if any farmers have reached an edge."""
        for farmer in self.farmers.sprites():
            if farmer.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for farmer in self.farmers.sprites():
            farmer.rect.y += self.settings.farmer_drop_speed
        self.settings.farmer_direction *= -1
    
    def _update_farmers(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.farmers.update()

        # Check for farmer-fox collision and respond accordingly.
        self._check_farmer_fox_collisions()
        # Check for farmers that reached thhe bottom of the screen.
        self._check_farmers_bottom()

        # Level up if all the farmers are shot down.
        self._level_up()
    
    def _check_farmer_fox_collisions(self):
        """Check for collisions between farmers and the fox."""
        if pygame.sprite.spritecollideany(self.fox, self.farmers):
            self._fox_hit()
    
    def _check_farmers_bottom(self):
        """Check if any farmers have reached the bottom of the screen."""
        for farmer in self.farmers.sprites():
            if farmer.rect.bottom >= self.screen.get_rect().bottom:
                # Treat this the same as if the fox got hit.
                self._fox_hit()
                break
    
    def _level_up(self):
        """Destroy bullets, make a new fleet and increase difficulty."""
        if not self.farmers:
            self._empty_sprites()
            self._make_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
    
    def _fox_hit(self):
        """Respond to the fox being hit by a farmer or a bullet."""
        if self.stats.fox_life > 0:
            # Decrement fox_left, and update scoreboard.
            self.stats.fox_life -= 1
            self.sb.prep_foxs()

            # Get rid of any remaining bullets and farmers.
            self._empty_sprites()

            self._make_fleet()
            self.fox.center_fox()

            # Pause the game.
            sleep(0.5)
        else:
            self.game_active = False
            self._make_difficulty_levels_buttons()
            self._stop_music()
            self.sounds.end_game.play()
            pygame.mouse.set_visible(True)

    def _fire_bullet(self):
        """Make a new bullet and add it to the bullets group."""
        if (self.game_active) and (not self.game_paused):
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

                # Play a sound when firing.
                self.sounds.fox_fire.play()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        
        # Get rid of old bullets when they disappear from the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        # Check for bullet-farmer collisions and respond.
        self._check_bullet_farmer_collisions()

        # Play a sound when a farmer is hit.
        self._farmer_hit_sound()

    def _check_bullet_farmer_collisions(self):
        """Respond to collisions between bullets and farmers."""
        self.collisions = pygame.sprite.groupcollide(self.bullets, 
                self.farmers, True, True)
        
        # Increment the score if there is a collision.
        self._increment_score()
    
    def _increment_score(self):
        """Increment the score when farmers are hit."""
        if self.collisions:
            for farmers in self.collisions.values():
                self.stats.score += self.settings.farmer_points * len(farmers)
            self.sb.prep_score()
            self.sb.check_high_score()
    
    def _farmer_hit_sound(self):
        """Play a sound when a farmer is hit by a bullet."""
        if self.collisions:
            self.sounds.farmer_death.play()

    def _make_farmer_bullet(self):
        """Make a new farmer's bullet and add it to the farmer_bullets group."""
        if len(self.farmer_bullets) < self.settings.farmer_bullets_allowed:
            new_farmer_bullet = FarmerBullet(self)
            self.farmer_bullets.add(new_farmer_bullet)
    
    def _check_farmers(self):
        """Check if farmers are added to the group and make farmer's bullets."""
        if self.farmers:
            self._make_farmer_bullet()

    def _fire_farmer_bullet(self):
        """Fire the farmers' bullets at random intervals."""
        if random() < self.settings.shooting_frequency:
            self._check_farmers()

    def _update_farmer_bullets(self):
        """Update farmers' bullets position and get rid of their old bullets."""
        self.farmer_bullets.update()

        # Get rid of old farmers' bullets.
        for farmer_bullet in self.farmer_bullets.copy():
            if farmer_bullet.rect.top >= self.screen.get_rect().bottom:
                self.farmer_bullets.remove(farmer_bullet)
        
        # Check for farmers' bullets and fox collisions and respond.
        self._check_farmer_bullet_fox_collisions()

    def _check_farmer_bullet_fox_collisions(self):
        """Respond to collisions between farmers' bullets and the fox."""
        if pygame.sprite.spritecollideany(self.fox, self.farmer_bullets):
            self._fox_hit()

    def _stop_music(self):
        """Stop all music if the fox has no lives left."""
        pygame.mixer.music.stop()
        self.sounds.fox_fire.stop()
        self.sounds.farmer_death.stop()
    
    def _draw_fox_objects(self):
        """Draw fox related objects."""
        self.bullets.draw(self.screen)
        self.fox.blitme()

    def _draw_farmer_objects(self):
        """Draw farmer related objects."""
        self.farmer_bullets.draw(self.screen)
        self.farmers.draw(self.screen)

    def _draw_buttons(self):
        """Draw the buttons for the game based on the current state."""
        self._draw_game_state_buttons()
        self._draw_menu_buttons()
    
    def _draw_game_state_buttons(self):
        """Draw the game state buttons."""
        if not self.game_active:
            self.play_button.draw_button()

        if not self.game_paused:
            self.pause_button.draw_button()
    
        if (self.game_paused) and (not self.game_restarted):
            self.resume_button.draw_button()

        if (self.game_paused) and (self.game_restarted):
            self.restart_button.draw_button()
        
        if self._are_credits_and_hotkeys_not_displayed():
            self.sb.show_score()

    def _draw_menu_buttons(self):
        """Draw the buttons related to the menu."""
        if (not self.game_active) or (self.game_paused):
            self.menu_button.draw_button()

        if self.sub_menu:
            self.difficulty_button.draw_button()
            self.hotkeys_button.draw_button()
            self.credits_button.draw_button()
        
        if self.show_credits:
            self.credits_display_button.draw_button()
            self.exit_button.draw_button()
        
        if self.show_hotkeys:
            self.hotkeys_display_button.draw_button()
            self.exit_button.draw_button()
        
        if (
            (self.difficulty_levels) 
            and (self._are_credits_and_hotkeys_not_displayed())
        ):
            self.easy_diff_button.draw_button()
            self.medium_diff_button.draw_button()
            self.hard_diff_button.draw_button()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.settings.background, (0, 0))
        self._draw_fox_objects()
        self._draw_farmer_objects()
        self._draw_buttons()
    
        pygame.display.flip()
    
    def _save_high_score_and_exit(self):
        """Save the high score when the user quits the game and exit."""
        saved_high_score = self.stats.read_high_score()
        if self.stats.high_score > saved_high_score:
            path = Path('high_score/high_score.json')
            high_score = json.dumps(self.stats.high_score)
            path.write_text(high_score)
        
        sys.exit()


if __name__ == '__main__':
    # Generate the instance to run the game.
    h_fox = HungryFox()
    h_fox.run_game()