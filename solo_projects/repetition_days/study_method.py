# Make a spaced repetion pop up to generate what to study/repeat each day.
# For convenience, create an alias in Bash to run the script every day.

import tkinter as tk
from datetime import datetime

days = [
    'monday', 
    'tuesday', 
    'wednesday', 
    'thursday', 
    'friday', 
    'saturday', 
    'sunday'
]

months = [
    'january', 
    'february', 
    'march', 
    'april', 
    'may', 
    'june', 
    'july', 
    'august', 
    'september', 
    'october', 
    'november', 
    'december'
]

# Create a study method for one subject.
# Generalize it so it works with any subject.
study_method = {
    'monday': [
        'Study new block', 
        'Repeat today\'s block'
    ], 
    'tuesday': [
        'Repeat yesterday\'s block', 
        'Study new block', 
        'Repeat today\'s block'
    ], 
    'wednesday': [
        'Repeat yesterday\'s block', 
        'Study new block', 
        'Repeat today\'s block'
    ], 
    'thursday': [
        'Repeat yesterday\'s block', 
        'Study new block', 
        'Repeat today\'s block'
    ], 
    'friday': [
        'Repeat Monday\'s block', 
        'Repeat yesterday\'s block', 
        'Study new block', 
        'Repeat today\'s block'
    ], 
    'saturday': [
        'Repeat all blocks'
    ], 
    'sunday': [
        'Repeat all blocks'
    ]  
}

subject1 = "python crash course"

# Function to display the pop-up message.
def show_popup():
    """
    Generate a pop-up window displaying the current date, 
    the subject being studied, and the tasks for the day.

    The pop-up window includes:
    - The current date in the format: "Day Month Year".
    - The title of the subject being studied.
    - Tasks scheduled for the current day based on the study method.

    Study tasks are determined based on the current day of the week
    and defined in the 'study_method' dictionary. Each day's tasks
    are listed according to the 'study_method' schedule.

    The pop-up window remains open until the user closes it.
    """
    # Get the current date.
    current_date = datetime.now().date()
    # Format the date as a string.
    formatted_date_day = current_date.strftime("%d")
    formatted_date_year = current_date.strftime("%Y")
    # Get the day of the week and month.
    day_of_week = current_date.weekday()
    month = current_date.month - 1
    # Convert the numeric day and moth to a string.
    day_name = days[day_of_week]
    month_name = months[month]
    # Generate the pop-up.
    popup = tk.Tk()
    popup.title("Spaced Repetition Reminder")
    # Create the main label.
    label = tk.Label(popup, 
                     text=f"{day_name.title()} "
                     f"{formatted_date_day} "
                     f"{month_name.title()} "
                     f"{formatted_date_year}")
    label.pack()
    # Additional label for book/subject title.
    subject = tk.Label(popup,
                       text=f"{subject1.title()}:",
                       foreground="dark red")
    subject.pack()
    # Text for each day study/repetition.
    for day, task in study_method.items():
        for i in range(4):
            if day_name == day:
                if i > len(task) -1:
                    break
                repetition_title = tk.Label(popup, 
                                            text=f"Today's task {i + 1}:",
                                            foreground="dark blue")
                repetition_title.pack(anchor="w")

                repetition = tk.Label(popup,
                                  text=f"- {task[i]}.")
                repetition.pack(anchor="w")
    
    popup.mainloop()

show_popup()