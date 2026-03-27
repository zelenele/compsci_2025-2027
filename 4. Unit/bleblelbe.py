# IB DP CompSci - Exception Handling Exercise


# ---------------------------------------------------------------------------
# PART 1 – VALUEERROR (safe integer input)
# ---------------------------------------------------------------------------

# TODO:
# - Ask the user for an integer
# - If they enter something invalid (like "abc"), print a helpful message
# - Keep asking until they enter a valid integer
# - Finally print: "You entered: <number>"

# Hint: use a while loop + try/except ValueError

number = None

# TODO: write your loop here
while True:
    number= input("Give me an intiger ")
    try:
        number = int(number)
    except ValueError:
        print("give a valid number ")
    else:
        print(f"Your nuber is {number}")
        break
    



# ---------------------------------------------------------------------------
# PART 2 – ZERODIVISIONERROR (safe division)
# ---------------------------------------------------------------------------

# TODO:
# - Ask the user for two integers: a and b
# - Print a / b
# - Handle:
#   1) ValueError (invalid integer input)
#   2) ZeroDivisionError (b == 0)
# - If an error happens, print a message and ask again

# TODO: write your loop here
numberA = None 
numberB = None

while True:
    numberA = input("Give me a number for A ")
    numberB = input("Give me number for B ")
    try:
        numberA = int(numberA)
        numberB = int(numberB)
    except ValueError:
        print("Make sure to put numbers in both cases") 
        continue
    try: 
        numberA / numberB
      
    except ZeroDivisionError:
        print("Number B is a zero it cant be")
    else:
        print(f"{numberA/numberB} is the division fo a/b")
        
# ---------------------------------------------------------------------------
# PART 3 – VALUEERROR (parsing data safely)
# ---------------------------------------------------------------------------

# TODO:
# - You are given a list of strings below.
# - Convert each value to an int and add to a total.
# - If a value is not a valid integer, skip it and print:
#   "Skipping invalid value: <value>"
#
# Note: Some values look like numbers but are NOT valid ints (e.g. "3.14").

total = 0

raw_values = ["10", "20", "hello", "30", "-5", "3.14", "40"]

# TODO: write your code here

print("Total of valid numbers:", total)


# ---------------------------------------------------------------------------
# PART 4 – DICTIONARY KEYERROR (safe lookup)
# ---------------------------------------------------------------------------

# TODO:
# - Use the dictionary below
# - Ask the user for a student name
# - Print their score
# - If the name is missing, do NOT crash. Print: "Student not found."
#
# You can solve this with either:
# - try/except KeyError
# - OR dict.get() (recommended)

mydictionary = {
    "songs": ["Song A", "Song B", "Song C"], # "songs" = key
    "games": ["Game X", "Game Y", "Game Z"], # list of games = value
    "grades": ["A", "B", "C"],
    "age": 21,
    "name": "Alice",
}
mydictionary["age"] # Example of accessing a value
mydictionary["age"] = 2500 # Example of modifying a value
mydictionary["country"] = input("Enter country: ") # Example of adding a new key/value pair
scores = {
    "Murrowak": 92,
    "Gyfin": 78,
    "Rhasia": 88,
    "Dokkaebi": 81,
}

# TODO: write your code here


# ---------------------------------------------------------------------------
# EXTENSION (optional)
# ---------------------------------------------------------------------------

# 1) Add a function safe_int_input(prompt) -> int that keeps asking until valid.
# 2) Add a function safe_open_read_text(path) -> list[str] that returns [] if missing.
# 3) Use your functions to reduce repeated code.