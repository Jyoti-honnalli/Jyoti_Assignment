import re

# Take password input
password = input("Enter your password: ")

score = 0
suggestions = []

# Check length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters")

# Check uppercase
if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add uppercase letters")

# Check lowercase
if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add lowercase letters")

# Check numbers
if re.search(r"[0-9]", password):
    score += 1
else:
    suggestions.append("Add numbers")

# Check special characters
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    suggestions.append("Add special characters")

# Strength result
if score <= 2:
    strength = "Weak ❌"
elif score <= 4:
    strength = "Medium ⚠️"
else:
    strength = "Strong ✅"

# Output
print("\nPassword Strength:", strength)
print("Score:", score, "/5")

if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)