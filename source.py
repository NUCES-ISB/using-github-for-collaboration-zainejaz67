# A simple Python program

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their age
age = int(input("How old are you? "))

# Calculate the year when the user will turn 100
current_year = 2024
year_turn_100 = current_year + (100 - age)

# Print a personalized greeting
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"You will turn 100 years old in the year {year_turn_100}.")
