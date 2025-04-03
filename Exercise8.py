# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Option 1: Search for a predefined name
search_name = "Sam"
if search_name in names:
    print(f"{search_name} was found in the list!")
else:
    print(f"{search_name} was not found in the list.")

# Option 2: Allow user to input a name to search
user_search = input("Enter a name to search: ").strip()
if user_search in names:
    print(f"{user_search} was found in the list!")
else:
    print(f"{user_search} was not found in the list.")
