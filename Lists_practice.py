

# PLEASE READ

# run this program. you will be asked a question as to how many steps you took during a certain day. 
# enter your steps for each day. at the end, you will receive your total amount and average amount of steps taken for the week.


#days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# steps
steps = []

# Loop of steps
for day in days:
    steps_taken = int(input(f"How many steps did you take on {day}? "))
    steps.append(steps_taken)

# steps per day
print("\nSteps recorded for each day:")
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")

# total steps
total_steps = sum(steps)
print(f"\nTotal steps taken in the week: {total_steps}")

# average steps
average = round(total_steps / len(steps))
print(f"Average steps per day: {average}")
