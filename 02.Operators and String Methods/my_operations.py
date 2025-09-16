# IB DP CompSci - Week 2 Exercise: Operators and String Methods

# ARITHMETIC OPERATORS
# Practice with basic math operations
num1 = 15
num2 = 4

# Complete the arithmetic operations
addition = num1 + num2
print(addition)

# TODO: Calculate subtraction
subtraction = num1 - num2
print(subtraction)

# TODO: Calculate multiplication
multiplication = num1 * num2
print(multiplication)

# TODO: Calculate division
division = num1 / num2
print(division)

# TODO: Calculate floor division
floor_division = num1 // num2
print(floor_division)

# TODO: Calculate modulus (remainder)
modulus = num1 % num2
print(modulus)

# Order of operations - what will be printed?
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(result1)  # Write your guess as a comment
print(result2)  # Write your guess as a comment

# COMPARISON OPERATORS
# Compare ages
your_age = 16
friend_age = 17

print(your_age > friend_age)   # Are you older? false
print(your_age == friend_age)  # Same age? false
print(your_age < friend_age)   # Are you younger? true

# TODO: Check if you are at least 16
at_least_16 = your_age >= 16
print(at_least_16)

# TODO: Check if your friend is not 18
friend_not_18 = friend_age != 18
print(friend_not_18)

# LOGICAL OPERATORS
# Weather decisions
temperature = 22
is_raining = False
is_weekend = True

# Can go to beach if warm and not raining
can_go_beach = temperature > 20 and not is_raining
print(can_go_beach)

# TODO: Should study inside if raining OR it's a weekday
should_study = is_weekend == False or is_raining == True
print(should_study)

# TODO: Wear jacket if cold OR raining
wear_jacket = temperature < 10 or is_raining
print(wear_jacket)

# STRING METHODS - BASIC
# Clean up a name
messy_name = "  bungee J. UMPERTON   "
print(messy_name.strip().title())

#TODO: Remove spaces and fix capitalization
clean_name = "Bungee j. umperton"
print(clean_name.strip().title())

# String information
sentence = "Python programming is fun!"
print(len(sentence))        # Length
print(sentence.upper())     # Uppercase
print(sentence.lower())     # Lowercase

# TODO: Count how many 'a' letters
sentancea = "Python programming is fun!aaaaaa"
count_a = sentancea.count("a")
print(count_a)

# TODO: Check if starts with 'Python'
starts_python = ("Python programming is fun!")
print(starts_python.startswith("Python"))

# TODO: Check if ends with '!'
ends_exclamation = ("Python programming is fun!")
print(ends_exclamation.endswith("exe"))

# STRING METHODS - REPLACING
message = "I love Java programming"

# Replace Java with Python
new_message = message.replace("Java", "Python")
print(message)
print(new_message)

# STRING SPLITTING
full_name = "John Michael Smith"
name_parts = full_name.split()
print(name_parts)
print(name_parts[0])  # First name
print(name_parts[-1]) # Last name

# Email processing
email = "student@school.edu"
email_parts = email.split("@")
username = email_parts[0]
domain = email_parts[1]
print(username)
print(domain)

# COMBINING CONCEPTS
# Grade calculator
student = "alex johnson"
math = 85
science = 92
english = 78

#TODO: Calculate average
average = None

#TODO: Format student name
formatted_student = None

print(formatted_student)
print(average)

# TODO: Check if student passed (average >= 80)
passed = None
print(passed)

# String validation
test_string = "12345"

# TODO: Check if all digits
all_digits = None
print(all_digits)

# TODO: Check if contains letters
has_letters = None
print(has_letters)

# CHALLENGE: Text analysis
text = "The quick brown fox"
words = text.split()
word_count = len(words)
char_count = len(text)

print(word_count)
print(char_count)

# Write your guesses as comments, then run and check