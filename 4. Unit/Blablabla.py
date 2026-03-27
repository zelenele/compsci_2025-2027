# IB DP CompSci - B2.5 File Processing Exercise

from __future__ import annotations

from pathlib import Path
import json

# ---------------------------------------------------------------------------
# SETUP – paths you can rely on
# ---------------------------------------------------------------------------

# This makes your file paths work even if you run the program from a different folder.
UNIT_DIR = Path(__file__).parent
DATA_DIR = UNIT_DIR / "data"

NOTES_PATH = DATA_DIR / "notes.txt"
SCORES_PATH = DATA_DIR / "scores.csv"
STUDENTS_PATH = DATA_DIR / "students.json"
ACCESS_LOG_PATH = DATA_DIR / "access.log"

OUTPUT_DIR = UNIT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# PART 1 – READING A TEXT FILE (notes.txt)
# ---------------------------------------------------------------------------

# TODO:
# - Read the entire file from NOTES_PATH (utf-8)
# - Count:
#   1) number of lines
#   2) number of words
#   3) number of characters (including spaces)
# - Print the results
#
# Hints:
# - Use: with open(NOTES_PATH, "r", encoding="utf-8") as f:
# - You can loop: for line in f:
# - Use .strip() to remove the newline

line_count = 0
word_count = 0
char_count = 0

# TODO: write your code here

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)


# ---------------------------------------------------------------------------
# PART 2 – WRITING OUTPUT (summary.txt)
# ---------------------------------------------------------------------------

# TODO:
# - Create an output file called summary.txt inside OUTPUT_DIR
# - Write a small report with the three values from Part 1
# - Then append one extra line: "Processed successfully"
#
# Required:
# - Use mode "w" first, then mode "a" (append)

SUMMARY_PATH = OUTPUT_DIR / "summary.txt"

# TODO: write your code here


# ---------------------------------------------------------------------------
# PART 3 – CSV PROCESSING (scores.csv)
# ---------------------------------------------------------------------------

# scores.csv format:
# name,math,science,english
# Steve,85,90,78
# ...

# TODO:
# - Read SCORES_PATH
# - Build a list of records, where each record is a dict like:
#   {"name": "Steve", "math": 85, "science": 90, "english": 78}
# - Then compute and print:
#   1) each student's average
#   2) the class average for each subject
#   3) the student with the highest average

records: list[dict] = []

# TODO: write your code here


# ---------------------------------------------------------------------------
# PART 4 – JSON PROCESSING (students.json)
# ---------------------------------------------------------------------------

# students.json format:
# [
#   {"name": "Alicja", "grade": 10, "club": "Robotics"},
#   ...
# ]

# TODO:
# - Load the JSON list from STUDENTS_PATH
# - Ask the user for a club name (e.g. "Robotics")
# - Print all students who are in that club
# - Add a new student (ask user for name/grade/club)
# - Write the updated list to OUTPUT_DIR/students_out.json (pretty printed)

STUDENTS_OUT_PATH = OUTPUT_DIR / "students_out.json"

# TODO: write your code here


# ---------------------------------------------------------------------------
# PART 5 – LOG FILE CHALLENGE (access.log)
# ---------------------------------------------------------------------------

# access.log format (one request per line):
# 2026-02-01 10:00:00 IP=10.0.0.5 PATH=/index STATUS=200

# TODO:
# - Count how many times each STATUS code appears (e.g. 200, 404, 500)
# - Find the top 3 IP addresses by request count
# - Print both results in a readable way
#
# Hints:
# - Each line contains "IP=" and "STATUS="
# - Use a dictionary as a frequency table

status_counts: dict[str, int] = {}
ip_counts: dict[str, int] = {}

# TODO: write your code here


# ---------------------------------------------------------------------------
# EXTENSION (optional)
# ---------------------------------------------------------------------------

# 1) Add error handling for missing files (FileNotFoundError)
# 2) Add validation for score conversion (ValueError)
# 3) Write your Part 3 results into OUTPUT_DIR/scores_report.txt