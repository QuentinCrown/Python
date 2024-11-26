def main():

    # date and time please
    date_time = input("Enter the current date and time (e.g., YYYY-MM-DD HH:MM): ")
    # diary entry
    entry = input("Write your diary entry: ")

    # open the file
    with open("personal_diary/diary.txt", "a") as diary_file:
        # date and time, the entry, and a blank line to separate entries
        diary_file.write(f"Date and Time: {date_time}\n")
        diary_file.write(f"Entry: {entry}\n")
        diary_file.write("\n")  # blank line

    print("Your entry has been saved to 'diary/diary.txt'.")

if __name__ == "__main__":
    main()
