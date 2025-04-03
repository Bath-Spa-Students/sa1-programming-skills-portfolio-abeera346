 # Dictionary mapping month numbers to number of days
month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Prompt user for the month number
month = int(input("Enter the month number (1-12): "))

# Validate the month number
if 1 <= month <= 12:
    # Special handling for February due to leap years
    if month == 2:
        is_leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if is_leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        # Print the number of days in the selected month
        print(f"The month {month} has {month_days[month]} days.")
else:
    # Handle invalid input
    print("Invalid month number. Please enter a number between 1 and 12.")
