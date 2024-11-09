# Program to check if there is a vowel in a string
string = input("Enter a String: ")
vowels = "aeiouAEIOU"
# Initialize a flag
contains_vowel = False

# Check each character in the string
for char in string:
    if char in vowels:
        contains_vowel = True
        break

# Output the result based on the flag
if contains_vowel:
    print("The string contains a vowel.")
else:
    print("The string does not contain any vowel.")

