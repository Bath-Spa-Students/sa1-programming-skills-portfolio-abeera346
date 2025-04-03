 def is_even_or_odd(number):
    """Check if the number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    """Prompt the user for a number and display whether it's even or odd."""
    try:
        num = int(input("Enter a number: "))  # Get user input
        print(is_even_or_odd(num))  # Print result
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
