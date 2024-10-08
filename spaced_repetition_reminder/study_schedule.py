#!/usr/bin/env python3

"""
This module imports the 'StudyPopUp' class from the pop_up module
to generate what to study/repeat each day.
It sets up a study schedule for each day of the week and defines the subject to
be studied.

For convenience, consider creating a terminal alias to run the script each day.
"""

from pop_up import StudyPopUp

# Define the parameters.
DAYS: list[str] = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

MONTHS: list[str] = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

STUDY_METHOD: dict[str, list[str]] = {
    "monday": ["Study new block", "Repeat today's block"],
    "tuesday": ["Repeat yesterday's block", "Study new block", "Repeat today's block"],
    "wednesday": [
        "Repeat yesterday's block",
        "Study new block",
        "Repeat today's block",
    ],
    "thursday": ["Repeat yesterday's block", "Study new block", "Repeat today's block"],
    "friday": [
        "Repeat Monday's block",
        "Repeat yesterday's block",
        "Study new block",
        "Repeat today's block",
    ],
    "saturday": ["Repeat all blocks"],
    "sunday": ["Repeat all blocks"],
}

subject: str = "python crash course"

if __name__ == "__main__":
    # Make an instance of StudyPopUp to display the study reminder.
    show_popup = StudyPopUp(DAYS, MONTHS, STUDY_METHOD, subject)
