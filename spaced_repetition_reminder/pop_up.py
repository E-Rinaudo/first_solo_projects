#!/usr/bin/env python3

"""
This module defines the 'StudyPopUp' class, which creates a pop-up window using tkinter.
The pop-up displays information about the subject to study or repeat
each day, including tasks for the day and the current date.
"""

import tkinter as tk
from datetime import datetime, date


class StudyPopUp:  # pylint: disable=R0903
    """Make a pop-up window to display the subject being studied."""

    def __init__(
        self,
        days: list[str],
        months: list[str],
        study_method: dict[str, list[str]],
        subject: str,
    ) -> None:
        """Initialize the pop-up attributes."""
        self.days = days
        self.months = months
        self.study_method = study_method
        self.subject = subject
        self.day_of_week: int = 0
        self.formatted_date: str = ""

        # Get the current date in a neatly formatted string.
        self._get_date()

        # Generate the pop-up.
        self._make_popup()

    def _get_date(self) -> None:
        """Get and neatly format the current date."""
        current_date: date = datetime.now().date()

        # Get the current day and month as int.
        self.day_of_week = current_date.weekday()
        month: int = current_date.month - 1

        # Use the int to get the name of the days and months from days and months lists.
        day_name: str = self.days[self.day_of_week].title()
        month_name: str = self.months[month].title()

        # Format the date as a string.
        self.formatted_date = current_date.strftime(f"{day_name}, %d {month_name} %Y")

    def _make_popup(self) -> None:
        """Generate a pop-up window displaying the current date,
        the subject being studied, and the tasks for the day.
        """
        popup: tk.Tk = tk.Tk()
        self._customize_popup(popup)
        popup.mainloop()

    def _customize_popup(self, popup: tk.Tk) -> None:
        """Customize the pop-up."""
        popup.title("Spaced Repetition Reminder")

        # Main label.
        tk.Label(popup, text=f"{self.formatted_date}").pack()

        # Additional label for book/subject title.
        tk.Label(popup, text=f"{self.subject.title()}:", foreground="dark red").pack()

        self._repetition_text(popup)

    def _repetition_text(self, popup: tk.Tk) -> None:
        """Display the text to describe the repetition for the current day."""
        tasks: list[str] = self.study_method.get(self.days[self.day_of_week], [])
        for i, task in enumerate(tasks[:4]):
            tk.Label(popup, text=f"Today's task {i + 1}:", foreground="dark blue").pack(
                anchor="w"
            )
            tk.Label(popup, text=f"- {task}.").pack(anchor="w")
