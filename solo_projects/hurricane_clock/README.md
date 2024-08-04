# hurricane_clock

Hurricane Clock is a program designed to simulate timed exercise intervals for the Hurricane Hypertrophy month of NXT in Athlean-X, a popular fitness program created by Jeff Cavaliere.
It provides a structured interval training experience by prompting the user for workout details. It then runs a clock for each set, alternating between 20-second and 40-second intervals with sound cues for timing. This structure replicates the workout regimen outlined in the Hurricane Hypertrophy program within Athlean-X.

## Files

**hurricane_clock.py**:
This script contains two main classes:

- HurricaneWorkout: Prompts the user for workout details such as muscle group, number of sets, and type of exercise. It initiates the workout based on these inputs.
  
- HurricaneSob: Uses the details from HurricaneWorkout to structure the timed intervals, guiding the user through the workout with sound notifications.

## Dependencies

**OS**:
For system-level operations like playing sounds. (Python Standard Library)

**Time**:
For managing interval durations. (Python Standard Library)

## Usage

To start a workout session, execute hurricane_clock.py from your terminal or preferred IDE.
Follow the prompts to enter the details for your workout, then press 'ENTER' to begin. The program will guide you through the intervals, playing sound cues to mark the end of each interval.

## Contact

If you wish to get in touch or provide feedback, you can reach me via email at <enricorinaudo91@gmail.com>.

Happy exercising!
