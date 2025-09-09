# Week 02 - Operators and String Methods

## Introduction

This week, we'll be taking a look at operators and string methods in Python. Operators are special symbols that perform operations on variables and values. String methods are built-in functions that allow you to manipulate and work with strings in various ways.

## Operators

You can think of operators as mathematical symbols that perform calculations or operations on numbers and variables. For example, the `+` operator is used for addition, while the `*` operator is used for multiplication. There are also comparison operators like `==` (equal to) and `!=` (not equal to) that allow you to compare values.

There are several types of operators in Python, including:

- Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical operators: `and`, `or`, `not`

You can find a complete list of operators in Python in W3Schools' [Python Operators](https://www.w3schools.com/python/python_operators.asp) page.

## String Methods

String methods are built-in functions that allow you to manipulate and work with strings in various ways. Some common string methods include:

- `str[index]`: Accesses a character at a specific index in a string.
- `find()`: Returns the index of the first occurrence of a specified substring in a string. Returns -1 if the substring is not found.
- `rfind()`: Returns the index of the last occurrence of a specified substring in a string. Returns -1 if the substring is not found.
- `slice()`: Extracts a portion of a string based on specified start and end indices.
- `replace()`: Replaces occurrences of a specified substring with another substring.
- `split()`: Splits a string into a list of substrings based on a specified delimiter.
- `+`: Concatenates two or more strings together.
- `*`: Repeats a string a specified number of times.

IMPORTANT: String methods are called on string objects using dot notation. For example, to use the `find()` method on a string variable named `my_string`, you would write `my_string.find("substring")`.

MORE IMPORTANT: String methods do not modify the original string. Instead, they return a new string with the desired changes. Strings in Python are immutable, meaning they cannot be changed after they are created. As an example, using the `replace()` method will return a new string with the replacements, but the original string will remain unchanged. Therefore, if you want to keep the changes, you need to assign the result of the method to a new variable or overwrite the original variable.

You can find a complete list of string methods in Python in W3Schools' [Python String Methods](https://www.w3schools.com/python/python_strings_methods.asp) page.
