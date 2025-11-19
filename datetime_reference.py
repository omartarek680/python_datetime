"""
==============================================================
                    PYTHON DATETIME REFERENCE
==============================================================

Author: Omar Tarek
Description:
    This module provides a clean, organized reference for Python's
    datetime, date, time, timedelta, strftime formatting, and
    strptime parsing.

    Use this script as a quick cheat sheet while learning Python.

Sections included:
    - Getting current date & time
    - Creating custom datetime objects
    - Formatting with strftime
    - Parsing strings with strptime
    - Using timedelta for date arithmetic

==============================================================
"""

import datetime


# --------------------------------------------------------------
# 1) GET CURRENT DATE & TIME
# --------------------------------------------------------------
def display_current_datetime():
    """Displays the current date, time, and individual components."""
    now = datetime.datetime.now()

    print("\n=== CURRENT DATETIME ===")
    print("Full datetime         :", now)
    print("Year                  :", now.year)
    print("Month                 :", now.month)
    print("Day                   :", now.day)
    print("Hour                  :", now.hour)
    print("Minute                :", now.minute)
    print("Second                :", now.second)
    print("Time only             :", now.time())
    print("Time max              :", datetime.time.max)
    print("Time min              :", datetime.time.min)


# --------------------------------------------------------------
# 2) CUSTOM DATE & TIME OBJECTS
# --------------------------------------------------------------
def display_custom_dates():
    """Shows how to manually create datetime and date objects."""
    print("\n=== CUSTOM DATE OBJECTS ===")
    print("Custom datetime       :", datetime.datetime(1994, 11, 4))
    print("Custom date only      :", datetime.date(1994, 11, 1))


# --------------------------------------------------------------
# 3) STRFTIME FORMATTING
# --------------------------------------------------------------
def display_strftime_examples():
    """Demonstrates formatting datetime into strings."""
    now = datetime.datetime.now()

    print("\n=== STRFTIME FORMAT EXAMPLES ===")
    print("YYYY-MM-DD            :", now.strftime("%Y-%m-%d"))
    print("DD/MM/YYYY            :", now.strftime("%d/%m/%Y"))
    print("Month name            :", now.strftime("%B"))
    print("Short month name      :", now.strftime("%b"))
    print("Day name              :", now.strftime("%A"))
    print("Short day name        :", now.strftime("%a"))
    print("12-hour time          :", now.strftime("%I:%M %p"))
    print("24-hour time          :", now.strftime("%H:%M:%S"))


# --------------------------------------------------------------
# 4) TIMEDTA DELTA (DATE MATH)
# --------------------------------------------------------------
def display_timedelta_examples():
    """Shows date arithmetic using timedelta."""
    today = datetime.date.today()

    print("\n=== TIMEDELTA EXAMPLES ===")
    print("Today                 :", today)
    print("10 days from today    :", today + datetime.timedelta(days=10))
    print("10 days ago           :", today - datetime.timedelta(days=10))

    now = datetime.datetime.now()
    print("2 hours later         :", now + datetime.timedelta(hours=2))


# --------------------------------------------------------------
# 5) STRPTIME PARSING
# --------------------------------------------------------------
def display_strptime_examples():
    """Parses a string into a datetime object."""
    date_str = "2025-11-19 14:30"
    parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    print("\n=== STRPTIME PARSING ===")
    print("Original string       :", date_str)
    print("Parsed datetime       :", parsed)
    print("Parsed year           :", parsed.year)


# --------------------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------------------
def main():
    print("\n==============================================================")
    print("             PYTHON DATETIME REFERENCE - DEMO")
    print("==============================================================")

    display_current_datetime()
    display_custom_dates()
    display_strftime_examples()
    display_timedelta_examples()
    display_strptime_examples()

    print("\n==============================================================")
    print("                  END OF DATETIME REFERENCE")
    print("==============================================================\n")


# Standard entry point
if __name__ == "__main__":
    main()
