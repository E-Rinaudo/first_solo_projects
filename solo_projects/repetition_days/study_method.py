# Call the spaced repetion pop-up class to generate what to study/repeat each day.
# For convenience, create an alias in the terminal to run the script every day.


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
