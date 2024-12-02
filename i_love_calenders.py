import calendar
from datetime import datetime

def main():
    
    # current year
    current_year = datetime.now().year

    while True:
        try:
            # birth month
            birth_month = int(input("Enter your birth month (1-12): "))

            # good input?
            if 1 <= birth_month <= 12:
                break
            else:
                print("Invalid month. Please enter a number between 1 and 12.")
        except ValueError:
            # is it an integer?
            print("Invalid input. Please enter a valid integer between 1 and 12.")

    # calendar
    cal = calendar.TextCalendar()

    # calender with month and year
    birth_month_calendar = cal.formatmonth(current_year, birth_month)

    # display
    print("\nHere is the calendar for your birth month:")
    print(birth_month_calendar)

if __name__ == "__main__":
    main()
