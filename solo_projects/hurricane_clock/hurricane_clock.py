# Simulate timed exercise intervals for Hurricane Hypertrophy,
#   NXT Month 2 of Athleanx.

import os
import time


class HurricaneSob:
    """Represent the Hurricane Hypertrophy interval training structure."""

    def __init__(self):
        """
        Initialize instance of the Workout class.
        It prompts user for the muscle being worked,
        the number of sets and defines the type of exercise.
        """
        self.workout = HurricaneWorkout()

    def run_clock(self):
        """Create the exercise interval clock."""
        print(f"\nGet ready to blast your {self.workout.muscle}.")

        counter = 1
        while counter <= self.workout.sets:
            print(f"\n-  SOB {self.workout.exercise} Set {counter}:")

            # Run for 20 sec.
            print("\nRunning for 20 seconds...")
            time.sleep(17)
            [self._play_sound() for _ in range(3)]

            # Run for 40 seconds.
            print("Running for 40 seconds...")
            time.sleep(37)
            [self._play_sound() for _ in range(3)]

            counter += 1

        print(f"\nSOB {self.workout.exercise} completed.")

        self._restart_clock()

    def _restart_clock(self):
        """Restart the clock if the exercise is the SOB 320."""
        if self.workout.exercise == 320:
            self.workout.exercise = 160
            self.workout.sets = 4
            self.workout._workout_start()
            self.run_clock()

    def _play_sound(self):
        """
        Use the 'afplay' command to play a sound three times
        to simulate a countdown.
        """
        os.system("afplay /System/Library/Sounds/Ping.aiff")


class HurricaneWorkout:
    """Represent the Hurricane Hypertrophy workout."""

    def __init__(self):
        """
        Display a greet message.
        Then, determine the workout based on user inputs and start it.
        """
        print("\nAre you ready to start your workout?")

        self._workout_muscle()
        self._workout_sets()
        self._workout_exercise()
        self._workout_start()

    def _workout_muscle(self):
        """Ask user for muscle being worked."""
        print("\nWhich muscle are you training today?")
        self.muscle = input("Muscle: ").title()

    def _workout_sets(self):
        """Ask user for number of sets."""
        print("\nHow many sets (4 or 8)?")

        while True:
            try:
                self.sets = int(input("Sets: "))
            except ValueError:
                print("\nIncorrect selection.")
                print("Please, type a number (4 or 8).")
            else:
                if self.sets == 8 or self.sets == 4:
                    break
                else:
                    print("\nPlease, type the correct number of sets (4 or 8).")

    def _workout_exercise(self):
        """Determine the type of exercise."""
        if self.sets == 8:
            self.exercise = 320
        elif self.sets == 4:
            self.exercise = 160

    def _workout_start(self):
        """Start the workout."""
        self.start = input(
            f"\nPress 'ENTER' when ready to start " f"the SOB {self.exercise}."
        )


if __name__ == "__main__":
    # Run the workout session.
    workout_session = HurricaneSob()
    workout_session.run_clock()
