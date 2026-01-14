# IB DP CompSci - Data Structures Exercise

# ---------------------------------------------------------------------------
# PART 1 – LIST BASICS
# ---------------------------------------------------------------------------

# Create a shopping list with at least 4 items (all strings).
shopping_list = ["milk", "bread", "eggs", "cheese"]  # You can change these items, go ham (not too far)

# Print:
# - the first item
# - the last item
# - how many items are in the list
print(shopping_list[0])
print(shopping_list[-1])
print(len(shopping_list))

# TODO:
# - Add one new item to the END of the list
# - Remove one item by VALUE (not by index)(use remove() list method)
# Write your own code below this comment.

# TODO: write code here using append() and remove()

print("Updated shopping list:", shopping_list)


# ---------------------------------------------------------------------------
# PART 2 – LIST + LOOPS + CONDITIONALS
# ---------------------------------------------------------------------------

# We want to count how many items in the shopping list contain the letter "a".
# TODO:
# - Use a for loop over shopping_list
# - Use an if statement to check if "a" is in the item (lowercase)
# - Keep a counter and print the final result

count_with_a = 0  # TODO: update this inside your loop

# TODO: write a for loop over shopping_list here and update count_with_a

print("Items containing the letter 'a':", count_with_a)


# ---------------------------------------------------------------------------
# PART 3 – 2D LISTS (tables of data)
# ---------------------------------------------------------------------------

# We will store test scores for 3 students in 3 subjects:
# Structure: [ [math, science, english], ... ]
# Each inner list is ONE student.
scores = [
    [85, 90, 78],   # student Steve
    [92, 88, 95],   # student Hwoarang
    [70, 75, 80]    # student Asuka
]

# TODO: Print the math score of student 1,
#           and the English score of student 2 using indices.

# TODO: replace None with correct indexing expressions
hwoarang_math = scores[1][0]
asuka_english = scores[2][2]

print(f"Hwoarang math grade: {hwoarang_math}")
print(f"Asuka English grade: {asuka_english}")
# ----------------------------------------------------------------------

# TODO: Calculate the average score for student 0.
# Hint: use sum() and len(), OR a loop.

steve_total = None      # TODO: calculate total of scores[0]
steve_average = None    # TODO: calculate average
print(f"Steve average: {steve_average}")
for score in scores[0]:
    steve_total += score
steve_average = steve_average / len(scores[0])
print(f"Steves avarge is: {steve_average}")

# TODO: Calculate and print the average score for EACH student using a loop.
# Example output:
# Steve average: ...
# Hwoarang average: ...
# Asuka average: ...

# TODO: write a loop over scores here that prints each student's average


# ---------------------------------------------------------------------------
# PART 4 – STACKS (LIFO) USING LISTS
# ---------------------------------------------------------------------------

# A stack: Last-In-First-Out
# We use list.append() to PUSH, and list.pop() to POP from the TOP.

def push(stack, item):
    """Add item to the top of the stack."""
    # TODO: use append() to add item to the stack
    pass


def pop(stack):
    """Remove and RETURN the top item from the stack.
    If stack is empty, print a message and return None.
    """
    # TODO: check if the stack is empty before popping
    # TODO: otherwise, remove and RETURN the last item
    pass


def peek(stack):
    """RETURN the top item WITHOUT removing it.
    If stack is empty, return None.
    """
    # TODO: return the last item of the stack without removing it
    pass


def stack_is_empty(stack):
    """Return True if stack is empty, otherwise False."""
    # TODO: return True if the stack has length 0, otherwise False
    pass


def browser_history_demo():
    """Use the stack functions above to simulate browser history.

    TODO:
    - Start with an empty stack called history_stack
    - Push three "pages" (strings) onto the stack
    - Print the current page (top of stack)
    - Pop one page to go "back"
    - Print the new current page
    """
    # TODO: write your code here using push(), pop(), peek(), stack_is_empty()
    pass


# ---------------------------------------------------------------------------
# PART 5 – QUEUES (FIFO) USING LISTS
# ---------------------------------------------------------------------------

# A queue: First-In-First-Out
# Simplest (but not most efficient) way with lists:
# - enqueue -> list.append(item)
# - dequeue -> list.pop(0)

def enqueue(queue, item):
    """Add item to the BACK of the queue."""
    # TODO: use append() to add item to the queue
    pass


def dequeue(queue):
    """Remove and return the FRONT item from the queue.
    If queue is empty, print a message and return None.
    """
    # TODO: if queue is empty, print a message and return None
    # TODO: otherwise, remove and return the first item
    pass


def queue_is_empty(queue):
    """Return True if queue is empty, otherwise False."""
    # TODO: return True if the queue has length 0, otherwise False
    pass


# TODO: Use the queue functions to simulate a print queue:
# - Create an empty list print_queue
# - Ask the user (in a loop, like we did for shopping summative and exercise) for document names to add to the queue.
#   Stop when the user types "done" or presses Enter with nothing.
# - After that, dequeue and "print" (just print their names) until queue is empty.


def fill_print_queue():
    """Ask user for document names and add them to the queue.

    TODO:
    - Create an empty list called print_queue
    - Use a while loop to ask the user for document names
    - Stop when the user types "done" or presses Enter with nothing
    - Use enqueue(...) to add each document to the queue
    - Return the queue at the end
    """
    # Hint: use input(), strip(), and a while loop
    pass


def process_print_queue(print_queue):
    """Dequeue and print documents until the queue is empty.

    TODO:
    - While the queue is NOT empty
    - Use dequeue(...) to get the next document
    - Print something like: "Printing: {document}"
    """
    pass