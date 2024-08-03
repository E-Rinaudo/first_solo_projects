"""
This module imports the 'StudyPopUp' class from the pop_up module
to generate what to study/repeat each day.
It sets up a study schedule for each day of the week and defines the subject to
be studied.

For convenience, consider creating a terminal alias to run the script each day.
"""

from pop_up import StudyPopUp

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

MONTHS = [
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

STUDY_METHOD = {
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

subject = "python crash course"

if __name__ == "__main__":
    # Make the instance and generate the pop-up.
    show_popup = StudyPopUp(DAYS, MONTHS, STUDY_METHOD, subject)
