"""
This module uses classes to simulate timed exercise intervals for Hurricane Hypertrophy,
a popular workout program from Athleanx.

- 'HurricaneWorkout': Prompts the user for the workout details such as:
                      muscle group, number of sets, and type of exercise.
                      It also starts the workout.
- 'HurricaneSob': Uses the details obtained by the HurricaneWorkout class
                  to make a timed interval training structure.
"""

import os
import time


class HurricaneWorkout:
    """Represent the Hurricane Hypertrophy workout."""

    def __init__(self):
        """
        Display a greet message.
        Then, determine the workout based on user inputs and start it.
        """
        self.sets = 0
        self.exercise = 0

        print("\nAre you ready to start your workout?")

        self._workout_muscle()
        self._workout_sets()
        self._workout_exercise()
        self.workout_start()

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
                if self.sets in (8, 4):
                    break
                print("\nPlease, type the correct number of sets (4 or 8).")

    def _workout_exercise(self):
        """Determine the type of exercise."""
        if self.sets == 8:
            self.exercise = 320
        elif self.sets == 4:
            self.exercise = 160

    def workout_start(self):
        """Start the workout."""
        self.start = input(
            f"\nPress 'ENTER' when ready to start the SOB {self.exercise}."
        )


class HurricaneSob:
    """Represent the Hurricane Hypertrophy interval training structure."""

    def __init__(self):
        """Initialize the instance of the HurricaneWorkout class."""
        self.workout = HurricaneWorkout()

    def run_clock(self):
        """Create the exercise interval clock."""
        print(f"\nGet ready to blast your {self.workout.muscle}.")

        for workout_set in range(1, self.workout.sets + 1):
            print(f"\n-  SOB {self.workout.exercise} Set {workout_set}:")

            # Run the interval clock.
            self._run_interval(20)
            self._run_interval(40)

        print(f"\nSOB {self.workout.exercise} completed.")

        # Restart the clock if the interval completed was the SOB 320.
        self._restart_clock()

    def _run_interval(self, duration):
        """
        Run for the specified duration in seconds
        and play a sound three times to simulate a countdown.
        """
        print(f"Running for {duration} seconds...")
        time.sleep(duration - 3)
        for _ in range(3):
            os.system("afplay /System/Library/Sounds/Ping.aiff")

    def _restart_clock(self):
        """Restart the clock if the exercise completed was the SOB 320."""
        if self.workout.exercise == 320:
            self.workout.exercise = 160
            self.workout.sets = 4
            self.workout.workout_start()
            self.run_clock()


if __name__ == "__main__":
    # Run the workout session.
    workout_session = HurricaneSob()
    workout_session.run_clock()
