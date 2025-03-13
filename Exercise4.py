# Asking the capital of France
answer = input("What is the capital of France? ")

# Checking if the answer is correct or not
if answer.lower() == "paris":
    print("Correct! The capital of France is Paris.")
else:
    print("Wrong! The capital of France is Paris.")

    
 # List of countries and their capitals
quiz_data = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo"
}

# Function to conduct the quiz
def run_quiz():
    for country, correct_capital in quiz_data.items():
        # Ask the user for the capital of each country
        answer = input(f"What is the capital of {country}? ").strip()
        
        # Check if the answer matches the correct capital, ignoring case
        if answer.lower() == correct_capital.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_capital}.")

# Run the quiz
run_quiz()
