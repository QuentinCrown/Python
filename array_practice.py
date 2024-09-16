# READ ME
    # run the program. you will be asked to input your bpm in the terminal.
    # once all bpm has been entered, you will receive your average bpm for the day



# time of day slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# heart rate
heart_rates = []

# loop
for time in time_slots:
    while True:
        try:
            heart_rate = int(input(f"Enter your heart rate for {time} (in bpm): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # append to sublist
    heart_rates.append([time, heart_rate])

# total and average heart rate
total_heart_rate = sum([hr[1] for hr in heart_rates])
average_heart_rate = total_heart_rate / len(heart_rates)

# 
print("\nHeart rate readings for each time slot:")
for entry in heart_rates:
    print(f"{entry[0]}: {entry[1]} bpm")

# Display the average heart rate
print(f"\nAverage heart rate: {round(average_heart_rate, 2)} bpm")
