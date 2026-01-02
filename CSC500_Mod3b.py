# Get users current time
while True:
    current_time = int(input("Enter the current time (0–23): "))
    if 0 <= current_time <= 23:
        break
    else:
        print("Invalid input. Please enter a number between 0 and 23.")# Get users hours to wait

hours_to_wait = int(input("Enter the number of hours to wait: "))

# Calculations
alarm_time = (current_time + hours_to_wait) % 24

# Get AM/PM time
if alarm_time == 0:
    display_time = 12
    period = "AM"
elif alarm_time < 12:
    display_time = alarm_time
    period = "AM"
elif alarm_time == 12:
    display_time = 12
    period = "PM"
else:
    display_time = alarm_time - 12
    period = "PM"

# Results
print(f"The alarm will go off at {alarm_time}:00 ({display_time}:00{period}).")