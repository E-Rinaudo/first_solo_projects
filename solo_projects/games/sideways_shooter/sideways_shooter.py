import sys
from random import random
from time import time
import json
from pathlib import Path

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from buttons import Buttons
from hero import Hero
from bullet import Bullet
from alien import Alien
from alien_bullet import AlienBullet
from explosion import Explosion
from sound_effects import Sound


class SidewaysShooter:
    """Class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.sounds = Sound()
    
        self._make_screen()

        self.stats = GameStats(self)

        self._initialize_starting_game_buttons()
        
        self.sb = Scoreboard(self)
        self.hero = Hero(self)

        self._sprite_groups()
        self._make_fleet()
        self._initialize_flags()
    
    def _make_screen(self):
        """Generate the screen for the game."""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")
    
    def _sprite_groups(self):
        """Store the sprite groups of the game."""
        self.explosions = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
    
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
        """Main loop to run the game."""
        while True:
            self._check_events()

            if (self.game_active) and (not self.game_paused):
                self._make_mouse_invisible()
                self.hero.choose_image()
                self._make_fleet()
                self._update_aliens()
                self._fire_alien_bullet()
                self._update_alien_bullets()
                self.hero.update()
                self.sounds.hero_bullet_sound()
                self._update_bullets()
                self.explosions.update()
            
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
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            self._save_high_score_and_exit()
        else:
            self._check_keydown_hero_events(event)
            self._check_keydown_buttons_events(event)
        
    def _check_keydown_hero_events(self, event):
        """Respond to keypresses linked to the hero."""
        if event.key == pygame.K_UP:
            self.hero.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.hero.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            self.hero.space_pressed = True
        
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
        if event.key == pygame.K_UP:
            self.hero.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.hero.moving_down = False
        elif event.key == pygame.K_SPACE:
            self.hero.space_pressed = False

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
        """Start a new game when the player clicks Play."""
        play_clicked = self._is_button_clicked(self.play_button)
        if (
            (play_clicked) and (not self.game_active) 
            and (self._are_credits_and_hotkeys_not_displayed())
        ):
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

        # Get rid of any remaining bullets and aliens.
        self._empty_sprites()

        # Create the fleet and center the hero.
        self._make_fleet()
        self.hero.center_hero()
    
    def _prep_starting_scoreboard(self):
        """Make the score, level and hero images for the Scoreboard."""
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_heros()

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
        self.alien_bullets.empty()
        self.aliens.empty()
        self.explosions.empty()
    
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
        self.sounds.hero_fire.stop()
        self.sounds.alien_explosion.stop()
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
    
    def _choose_difficulty(self):
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
        if self.mouse_visible:
            current_time = time()
            if current_time - self.last_mouse_movement > mouse_inactivity_time:
                self.mouse_visible = False
                pygame.mouse.set_visible(self.mouse_visible)
    
    def _make_fleet(self):
        """Make an alien and add it to the aliens group."""
        # Generate aliens at random.
        if (
            (random() < self.settings.alien_frequency) 
            and (len(self.aliens) < self.settings.max_aliens)
        ):
            alien = Alien(self)
            self.aliens.add(alien)
    
    def _update_aliens(self):
        """Update aliens positions."""
        self.aliens.update()

        # Check for alien-hero collisions and respond.
        self._check_alien_hero_collisions()
        # Check for any alien that has reached the left side of the screen.
        self._check_aliens_left_side()
    
    def _check_alien_hero_collisions(self):
        """Check for collisions between aliens and the hero."""
        if pygame.sprite.spritecollideany(self.hero, self.aliens):
            self._hero_hit()
    
    def _check_aliens_left_side(self):
        """Check if any aliens have reached the left side of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= self.screen.get_rect().left:
                # Treat this the same as if the hero got hit.
                self._hero_hit()
                break
    
    def _hero_hit(self):
        """Respond to the hero being hit by an alien or a bullet."""
        if self.stats.hero_life > 0:
            # Decrement hero_life, and update scoreboard.
            self.stats.hero_life -= 1
            self.sb.prep_heros()
            # Reset the number of hit aliens, needed to increase level.
            self.settings.alien_hit = 0

            # Get rid of any remaining bullets and aliens.
            self._empty_sprites()

            self._make_fleet()
            self.hero.center_hero()
        else:
            self.game_active = False
            self._make_difficulty_levels_buttons()
            self._stop_music()
            self.sounds.end_game.play()
            pygame.mouse.set_visible(True)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if (self.game_active) and (not self.game_paused):
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

                # Play a sound when firing.
                self.sounds.hero_fire.play()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Delete old bullets.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.hero.screen_rect.right:
                self.bullets.remove(bullet)
        
        # Check for bullet-alien collisions.
        self._check_bullet_alien_collisions()

        # Generate an explosion when an alien is hit.
        self._make_explosion()
    
        # Level up if 10 aliens are shot down.
        self._level_up()

    def _check_bullet_alien_collisions(self):
        """Respond to collisions between bullets and aliens."""
        self.collisions = pygame.sprite.groupcollide(self.bullets, 
                self.aliens, True, True)
        
        # Increment the score if there is a collision.
        self._increment_score()
    
    def _increment_score(self):
        """Increment the score if aliens are hit."""
        if self.collisions:
            for aliens in self.collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
    
    def _make_explosion(self):
        """Make a new explosion and add it to the group."""
        if self.collisions:
            self.new_explosion = Explosion(self)
            self.explosions.add(self.new_explosion)

            # Play a sound when the alien explodes.
            self.sounds.alien_explosion.play() 

            # Position the explosition where the alien got hit.
            self._set_explosion()
    
    def _set_explosion(self):
        """Position the explosion after an alien has been hit."""
        for aliens in self.collisions.values():
            self.new_explosion.rect.center = aliens[0].rect.center
    
    def _level_up(self):
        """Increase difficulty if 10 aliens are hit."""
        if self.collisions:
            self.settings.alien_hit += 1
        
        if self.settings.alien_hit == self.settings.max_aliens:
            self.settings.increase_speed()
            self.settings.alien_hit = 0

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _make_alien_bullet(self):
        """Create a new aliens' bullet and add it to the alien_bullets group."""
        if len(self.alien_bullets) < self.settings.alien_bullets_allowed:
            new_alien_bullet = AlienBullet(self)
            self.alien_bullets.add(new_alien_bullet)
    
    def _check_aliens(self):
        """Check if aliens are added to the group and make the aliens' bullets."""
        if self.aliens:
            self._make_alien_bullet()

    def _fire_alien_bullet(self):
        """Fire the aliens' bullets at random intervals every 2 seconds."""
        if random() < self.settings.shooting_frequency:
            current_time = time()
            cooldown_time = 2
            if current_time > self.settings.shooting_cooldown + cooldown_time:
                self._check_aliens()
                self.settings.shooting_cooldown = current_time

    def _update_alien_bullets(self):
        """Update aliens' bullets position and get rid of old bullets."""
        self.alien_bullets.update()

        # Get rid of old aliens' bullets.
        for alien_bullet in self.alien_bullets.copy():
            if alien_bullet.rect.right <= self.screen.get_rect().left:
                self.alien_bullets.remove(alien_bullet)

        # Check for aliens' bullet and hero collisions and respond.
        self._check_alien_bullet_hero_collisions()

    def _check_alien_bullet_hero_collisions(self):
        """Respond to collisions between aliens' bullets and the hero."""
        if pygame.sprite.spritecollideany(self.hero, self.alien_bullets):
            self._hero_hit()

    def _stop_music(self):
        """Stop all music if the hero has no lives left."""
        pygame.mixer.music.stop()
        self.sounds.hero_fire.stop()
        self.sounds.alien_explosion.stop()
    
    def _draw_hero_objects(self):
        """Draw hero related objects."""
        self.bullets.draw(self.screen)
        self.hero.blitme()

    def _draw_alien_objects(self):
        """Draw alien related objects."""
        self.alien_bullets.draw(self.screen)
        self.aliens.draw(self.screen)
        self.explosions.draw(self.screen)
        
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
        self._draw_hero_objects()
        self._draw_alien_objects()
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
    # Create the instance and run the game.
    s_shooter = SidewaysShooter()
    s_shooter.run_game()