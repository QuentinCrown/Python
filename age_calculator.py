from datetime import datetime

def main():
    
    try:
        # birthday in YYYY-MM-DD format
        birthday_str = input("Enter your birthday (YYYY-MM-DD): ")

        # datetime object
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
        print(f"Your birthday is: {birthday.strftime('%A, %B %d, %Y')}")

        # current date and time
        now = datetime.now()

        # difference between now and the birthday
        delta = now - birthday

        # calculate years (accounts for leap years)
        years = delta.days // 365

        # calculate remaining days 
        remaining_days_after_years = delta.days % 365

        # estimate months (average days in a month)
        months = int(remaining_days_after_years / 30.44)

        # calculate weeks
        weeks = delta.days // 7

        # total days
        days = delta.days

        # calculate hours
        hours = days * 24

        # calculate minutes
        minutes = hours * 60

        # display
        print("\nYour Age in Different Units:")
        print(f"Years: {years}")
        print(f"Months: ~{years * 12 + months}")
        print(f"Weeks: {weeks}")
        print(f"Days: {days}")
        print(f"Hours: {hours}")
        print(f"Minutes: {minutes}")

    except ValueError:
        # invalid entry
        print("Invalid date format. Please enter your birthday in the format YYYY-MM-DD.")

if __name__ == "__main__":
    main()
