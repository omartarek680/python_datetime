"""
==============================================================
                    PYTHON DATETIME REFERENCE
==============================================================

Author: Omar Tarek (Improved Version)
Description:
    This module provides a clean, organized reference for Python's
    datetime, date, time, timedelta, strftime formatting, and
    strptime parsing.

    Use this script as a quick cheat sheet while learning Python.

Sections included:
    - Getting current date & time
    - Creating custom datetime objects
    - Format code reference
    - Formatting with strftime
    - Parsing strings with strptime
    - Using timedelta for date arithmetic
    - Date comparisons
    - Timezone handling
    - Practical examples
    - Error handling

==============================================================
"""

import datetime
from datetime import timezone, timedelta


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
    print("Microsecond           :", now.microsecond)
    print("Time only             :", now.time())
    print("Date only             :", now.date())
    print("Time max              :", datetime.time.max)
    print("Time min              :", datetime.time.min)


# --------------------------------------------------------------
# 2) CUSTOM DATE & TIME OBJECTS
# --------------------------------------------------------------
def display_custom_dates():
    """Shows how to manually create datetime and date objects."""
    print("\n=== CUSTOM DATE OBJECTS ===")
    print("Custom datetime       :", datetime.datetime(1994, 11, 4))
    print("Custom datetime (full):", datetime.datetime(1994, 11, 4, 14, 30, 45))
    print("Custom date only      :", datetime.date(1994, 11, 1))
    print("Custom time only      :", datetime.time(14, 30, 45))


# --------------------------------------------------------------
# 3) FORMAT CODE REFERENCE
# --------------------------------------------------------------
def display_format_codes():
    """Shows commonly used strftime/strptime format codes."""
    print("\n=== FORMAT CODE REFERENCE ===")
    codes = {
        "%Y": "Year (4 digits, e.g., 2025)",
        "%y": "Year (2 digits, e.g., 25)",
        "%m": "Month (01-12)",
        "%B": "Month name (January)",
        "%b": "Short month (Jan)",
        "%d": "Day of month (01-31)",
        "%A": "Weekday name (Monday)",
        "%a": "Short weekday (Mon)",
        "%H": "Hour 24h (00-23)",
        "%I": "Hour 12h (01-12)",
        "%M": "Minute (00-59)",
        "%S": "Second (00-59)",
        "%p": "AM/PM",
        "%f": "Microsecond (000000-999999)",
        "%j": "Day of year (001-366)",
        "%U": "Week number (Sunday first day)",
        "%W": "Week number (Monday first day)",
        "%w": "Weekday as number (0=Sunday)",
        "%z": "UTC offset (+0000)",
        "%Z": "Timezone name",
    }
    
    for code, description in codes.items():
        print(f"{code:5} -> {description}")


# --------------------------------------------------------------
# 4) STRFTIME FORMATTING
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
    print("ISO format            :", now.strftime("%Y-%m-%dT%H:%M:%S"))
    print("Full format           :", now.strftime("%A, %B %d, %Y at %I:%M %p"))
    print("Day of year           :", now.strftime("%j"))
    print("Week number           :", now.strftime("%U"))
    print("Custom format         :", now.strftime("%d-%b-%Y (%A)"))


# --------------------------------------------------------------
# 5) TIMEDELTA (DATE MATH)
# --------------------------------------------------------------
def display_timedelta_examples():
    """Shows date arithmetic using timedelta."""
    today = datetime.date.today()

    print("\n=== TIMEDELTA EXAMPLES ===")
    print("Today                 :", today)
    print("10 days from today    :", today + datetime.timedelta(days=10))
    print("10 days ago           :", today - datetime.timedelta(days=10))
    print("3 weeks from today    :", today + datetime.timedelta(weeks=3))

    now = datetime.datetime.now()
    print("\n2 hours later         :", now + datetime.timedelta(hours=2))
    print("90 minutes later      :", now + datetime.timedelta(minutes=90))
    print("30 seconds ago        :", now - datetime.timedelta(seconds=30))
    
    # Timedelta properties
    delta = datetime.timedelta(days=5, hours=3, minutes=30, seconds=45)
    print(f"\nTimedelta: {delta}")
    print(f"Total seconds         : {delta.total_seconds()}")
    print(f"Days component        : {delta.days}")
    print(f"Seconds component     : {delta.seconds}")


# --------------------------------------------------------------
# 6) STRPTIME PARSING
# --------------------------------------------------------------
def display_strptime_examples():
    """Parses a string into a datetime object."""
    date_str = "2025-11-19 14:30"
    parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    print("\n=== STRPTIME PARSING ===")
    print("Original string       :", date_str)
    print("Parsed datetime       :", parsed)
    print("Parsed year           :", parsed.year)
    print("Parsed month          :", parsed.month)
    
    # More parsing examples
    date_str2 = "25/12/2025"
    parsed2 = datetime.datetime.strptime(date_str2, "%d/%m/%Y")
    print("\nOriginal string       :", date_str2)
    print("Parsed datetime       :", parsed2)
    
    date_str3 = "Monday, November 19, 2025"
    parsed3 = datetime.datetime.strptime(date_str3, "%A, %B %d, %Y")
    print("\nOriginal string       :", date_str3)
    print("Parsed datetime       :", parsed3)


# --------------------------------------------------------------
# 7) DATE COMPARISON
# --------------------------------------------------------------
def display_comparison_examples():
    """Shows how to compare dates."""
    print("\n=== DATE COMPARISON ===")
    
    date1 = datetime.date(2025, 11, 19)
    date2 = datetime.date(2025, 12, 25)
    
    print(f"Date 1: {date1}")
    print(f"Date 2: {date2}")
    print(f"Date1 < Date2         : {date1 < date2}")
    print(f"Date1 > Date2         : {date1 > date2}")
    print(f"Date1 == Date2        : {date1 == date2}")
    print(f"Date1 != Date2        : {date1 != date2}")
    
    # Days between dates
    difference = date2 - date1
    print(f"\nDays between          : {difference.days} days")
    
    # Check if date is in the past/future
    today = datetime.date.today()
    past_date = datetime.date(2020, 1, 1)
    future_date = datetime.date(2030, 1, 1)
    
    print(f"\nToday                 : {today}")
    print(f"Is {past_date} in past? : {past_date < today}")
    print(f"Is {future_date} in future? : {future_date > today}")


# --------------------------------------------------------------
# 8) TIMEZONE HANDLING
# --------------------------------------------------------------
def display_timezone_examples():
    """Shows timezone-aware datetime objects."""
    print("\n=== TIMEZONE EXAMPLES ===")
    
    # UTC time
    utc_now = datetime.datetime.now(timezone.utc)
    print("UTC time              :", utc_now)
    
    # Custom timezone (e.g., EST = UTC-5)
    est = timezone(timedelta(hours=-5))
    est_now = datetime.datetime.now(est)
    print("EST time              :", est_now)
    
    # Custom timezone (e.g., IST = UTC+5:30)
    ist = timezone(timedelta(hours=5, minutes=30))
    ist_now = datetime.datetime.now(ist)
    print("IST time              :", ist_now)
    
    # Convert between timezones
    print("\nUTC to EST            :", utc_now.astimezone(est))
    print("UTC to IST            :", utc_now.astimezone(ist))
    
    # Naive vs aware datetimes
    naive = datetime.datetime.now()
    aware = datetime.datetime.now(timezone.utc)
    print(f"\nNaive datetime        : {naive} (tzinfo: {naive.tzinfo})")
    print(f"Aware datetime        : {aware} (tzinfo: {aware.tzinfo})")


# --------------------------------------------------------------
# 9) PRACTICAL EXAMPLES
# --------------------------------------------------------------
def display_practical_examples():
    """Shows real-world datetime use cases."""
    print("\n=== PRACTICAL EXAMPLES ===")
    
    # Calculate age
    birthdate = datetime.date(1994, 11, 4)
    today = datetime.date.today()
    age = (today - birthdate).days // 365
    print(f"Birthdate             : {birthdate}")
    print(f"Age (approx)          : {age} years")
    
    # Check if date is weekend
    some_date = datetime.date.today()
    weekday_num = some_date.weekday()  # 0=Monday, 6=Sunday
    is_weekend = weekday_num >= 5
    weekday_name = some_date.strftime("%A")
    print(f"\nToday is              : {weekday_name}")
    print(f"Is today weekend?     : {is_weekend}")
    
    # First day of month
    first_of_month = today.replace(day=1)
    print(f"\nFirst day of month    : {first_of_month}")
    
    # Last day of month
    if today.month == 12:
        next_month = today.replace(year=today.year + 1, month=1, day=1)
    else:
        next_month = today.replace(month=today.month + 1, day=1)
    last_of_month = next_month - datetime.timedelta(days=1)
    print(f"Last day of month     : {last_of_month}")
    
    # Days until specific date
    christmas = datetime.date(today.year, 12, 25)
    if christmas < today:
        christmas = datetime.date(today.year + 1, 12, 25)
    days_until = (christmas - today).days
    print(f"\nDays until Christmas  : {days_until} days")
    
    # Timestamp conversions
    now = datetime.datetime.now()
    timestamp = now.timestamp()
    from_timestamp = datetime.datetime.fromtimestamp(timestamp)
    print(f"\nDatetime              : {now}")
    print(f"Unix timestamp        : {timestamp}")
    print(f"From timestamp        : {from_timestamp}")


# --------------------------------------------------------------
# 10) ERROR HANDLING
# --------------------------------------------------------------
def display_error_handling():
    """Shows common datetime errors and how to handle them."""
    print("\n=== ERROR HANDLING ===")
    
    # Invalid date string
    print("Example 1: Invalid date format")
    try:
        bad_date = datetime.datetime.strptime("2025-13-40", "%Y-%m-%d")
    except ValueError as e:
        print(f"Caught error          : {e}")
    
    # Wrong format string
    print("\nExample 2: Wrong format string")
    try:
        wrong_format = datetime.datetime.strptime("2025-11-19", "%d/%m/%Y")
    except ValueError as e:
        print(f"Caught error          : {e}")
    
    # Safe parsing with default
    def safe_parse(date_str, format_str, default=None):
        """Parse date string safely with fallback."""
        try:
            return datetime.datetime.strptime(date_str, format_str)
        except ValueError:
            return default if default else datetime.datetime.now()
    
    print("\nExample 3: Safe parsing with fallback")
    result = safe_parse("invalid", "%Y-%m-%d", datetime.datetime.now())
    print(f"Safe parsing fallback : {result}")
    
    # Valid parsing
    result2 = safe_parse("2025-11-19", "%Y-%m-%d")
    print(f"Safe parsing success  : {result2}")


# --------------------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------------------
def main():
    print("\n==============================================================")
    print("             PYTHON DATETIME REFERENCE - DEMO")
    print("==============================================================")

    display_current_datetime()
    display_custom_dates()
    display_format_codes()
    display_strftime_examples()
    display_timedelta_examples()
    display_strptime_examples()
    display_comparison_examples()
    display_timezone_examples()
    display_practical_examples()
    display_error_handling()

    print("\n==============================================================")
    print("                  END OF DATETIME REFERENCE")
    print("==============================================================\n")


# Standard entry point
if __name__ == "__main__":
    main()
