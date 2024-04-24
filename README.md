# Julian Date Converter

This Python script converts a given date in the format (dd/mm/yyyy) along with time (in 12-hour format) to Julian Days.

### Requirements:
- Python 3

### How to Use:
1. Run the script.
2. Enter the date in the format (dd/mm/yyyy).
3. Enter the time in 12-hour format (hh:mm:ss).
4. Enter either 'AM' or 'PM' when prompted.
5. The script will output the Julian Date.

### How it Works:
- The script takes the input date and time.
- It calculates the number of days in the given year, month, and day.
- Adjusts for the transition from the Julian to the Gregorian calendar in 1582.
- Calculates the Julian Date and outputs it.

### Note:
- For years before 1582, the script does not account for the transition from the Julian to the Gregorian calendar.

