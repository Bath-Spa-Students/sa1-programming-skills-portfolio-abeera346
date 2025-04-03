# Define the correct password
correct_password = "Abeera"

# Set the maximum number of attempts
max_attempts = 5
attempts = 0

# Loop until the user enters the correct password or reaches max attempts
while attempts < max_attempts:
    entered_password = input("Enter the password: ")  # Ask user for password
    
    if entered_password == correct_password:
        print("You have successfully logged in.")  # Correct password message
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Maximum attempts reached. Authorities have been alerted .")  # Max attempts message
