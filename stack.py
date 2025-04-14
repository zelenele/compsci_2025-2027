"""Stack implementation using Python list
This module provides a basic Stack data structure implementation following
the Last-In-First-Out (LIFO) principle, with the underlying data structure
being a Python list.
Example:
    stack.push(1)   # Push 1 onto the stack
    stack.push(2)   # Push 2 onto the stack
    print(stack.peek())  # Outputs: 2
    print(stack.pop())   # Outputs: 2, removes 2 from the stack
    print(stack.is_empty())  # Outputs: False
Raises:
    IndexError: When attempting to pop or peek from an empty stack
Returns:
    Stack: A Stack object with LIFO behavior
"""


class Stack:
    """Stack(Last In First Out) implementation with a list(array) as the underlying data structure.
    This stack supports basic operations: push, pop; supports optional operations: peek, is_empty
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack.
        Raises IndexError if stack is empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it.
        Raises IndexError if stack is empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def display(self):
        """Return the list of items **FOR DISPLAY ONLY, NOT A PART OF STACK FUNCTIONALITY**."""
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    print("Stack created:", stack)
    print("Is stack empty?")
    print(stack.is_empty())
    print("Pushing 10 onto the stack")
    stack.push(10)
    print("Stack now:", stack.display())
    print("Pushing 20 onto the stack")
    stack.push(20)
    print("Stack now:", stack.display())

    print("Top element:", stack.peek())

    print("Popping:", stack.pop())
    print("Stack after pop:", stack.display())

    print("Is stack empty?", stack.is_empty())
