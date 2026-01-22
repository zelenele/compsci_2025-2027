
## 1) List basics (1D list)

### Create list + access first/last + length

```text
shopping_list ← ["milk", "bread", "eggs", "cheese"]

OUTPUT shopping_list[0]                 // first item
OUTPUT shopping_list[LENGTH(shopping_list) - 1]   // last item
OUTPUT LENGTH(shopping_list)            // number of items
```

### Add to end (append) + remove by value

```text
APPEND(shopping_list, "butter")
REMOVE_VALUE(shopping_list, "eggs")     // removes first matching value
OUTPUT shopping_list
```

---

## 2) List + loop + conditional (count items containing "a")

```text
count_with_a ← 0

FOR EACH item IN shopping_list DO
    IF CONTAINS(item, "a") THEN
        count_with_a ← count_with_a + 1
    ENDIF
ENDFOR

OUTPUT count_with_a
```

If they want it case-insensitive:

```text
IF CONTAINS(TO_LOWER(item), "a") THEN
```

---

## 3) 2D lists (table of data)

### Data structure

```text
scores ← [
  [85, 90, 78],   // Steve: math, science, english
  [92, 88, 95],   // Hwoarang
  [70, 75, 80]    // Asuka
]
```

### Access specific values (row, column)

```text
hwoarang_math ← scores[1][0]
asuka_english ← scores[2][2]

OUTPUT hwoarang_math
OUTPUT asuka_english
```

### Average for ONE student (Steve = row 0)

```text
total ← 0
FOR EACH mark IN scores[0] DO
    total ← total + mark
ENDFOR

average ← total / LENGTH(scores[0])
OUTPUT average
```

### Average for EACH student (loop over rows)

```text
student_names ← ["Steve", "Hwoarang", "Asuka"]

FOR i FROM 0 TO LENGTH(scores) - 1 DO
    total ← 0

    FOR EACH mark IN scores[i] DO
        total ← total + mark
    ENDFOR

    average ← total / LENGTH(scores[i])
    OUTPUT student_names[i] + " average: " + average
ENDFOR
```

---

## 4) Stack (LIFO) using a list

### Core stack operations

```text
PROCEDURE PUSH(stack, item)
    APPEND(stack, item)
ENDPROCEDURE
```

```text
FUNCTION POP(stack)
    IF LENGTH(stack) = 0 THEN
        OUTPUT "Stack is empty"
        RETURN NULL
    ELSE
        RETURN REMOVE_LAST(stack)   // removes and returns last element
    ENDIF
ENDFUNCTION
```

```text
FUNCTION PEEK(stack)
    IF LENGTH(stack) = 0 THEN
        RETURN NULL
    ELSE
        RETURN stack[LENGTH(stack) - 1]
    ENDIF
ENDFUNCTION
```

```text
FUNCTION STACK_IS_EMPTY(stack)
    RETURN (LENGTH(stack) = 0)
ENDFUNCTION
```

### Browser history demo (using stack)

```text
history_stack ← []

PUSH(history_stack, "google.com")
PUSH(history_stack, "wikipedia.org")
PUSH(history_stack, "ibocompsci.net")

OUTPUT "Current page: " + PEEK(history_stack)

POP(history_stack)   // go back

OUTPUT "Now on: " + PEEK(history_stack)
```

---

## 5) Queue (FIFO) using a list

### Core queue operations

```text
PROCEDURE ENQUEUE(queue, item)
    APPEND(queue, item)
ENDPROCEDURE
```

```text
FUNCTION DEQUEUE(queue)
    IF LENGTH(queue) = 0 THEN
        OUTPUT "Queue is empty"
        RETURN NULL
    ELSE
        RETURN REMOVE_FIRST(queue)   // removes and returns index 0
    ENDIF
ENDFUNCTION
```

```text
FUNCTION QUEUE_IS_EMPTY(queue)
    RETURN (LENGTH(queue) = 0)
ENDFUNCTION
```

### Fill print queue (inputs until "done" or empty)

```text
FUNCTION FILL_PRINT_QUEUE()
    print_queue ← []

    WHILE TRUE DO
        INPUT doc
        doc ← TRIM(doc)

        IF doc = "" OR doc = "done" THEN
            BREAK
        ENDIF

        ENQUEUE(print_queue, doc)
    ENDWHILE

    RETURN print_queue
ENDFUNCTION
```

### Process print queue (dequeue until empty)

```text
PROCEDURE PROCESS_PRINT_QUEUE(print_queue)
    WHILE NOT QUEUE_IS_EMPTY(print_queue) DO
        doc ← DEQUEUE(print_queue)
        OUTPUT "Printing: " + doc
    ENDWHILE
ENDPROCEDURE
```

## Big-O Cheat Sheet: Step-by-Step (with examples)

### Step 0: Decide what Big-O you’re giving

Unless the question says otherwise, assume:

* **Worst-case time complexity**
* And separately: **space complexity**

---

## Step 1: Define the input size (n)

Pick the variable that grows with the input.

**Example**

* If input is a list `arr`:
  $$
  n = \text{len(arr)}
  $$

---

## Step 2: Pick the “basic operation” to count

Choose something that happens repeatedly:

* comparisons (`==`, `<`, `in`)
* assignments
* loop iterations
* array accesses

**Example (duplicates code)**
Count comparisons like `arr[i] == arr[j]`.

---

## Step 3: Count how many times each loop runs

Use these exam rules:

### Rule A: Single loop over (n)

```text
for i in range(n):
```

Runs (n) times → **O(n)**

### Rule B: Nested loops multiply

```text
for i in range(n):
    for j in range(n):
```

Runs (n \times n = n^2) → **O(n²)**

### Rule C: Inner loop depends on i (triangle)

```text
for i in range(n):
    for j in range(i+1, n):
```

Runs:
$$
(n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2}
$$
Still grows like $n^2$ → **O(n²)**

---

## Step 4: Multiply/Combine costs, then simplify

### Common simplification rules

* **Drop constants:** $2n \rightarrow O(n)$
* **Drop lower terms:** $n^2 + n \rightarrow O(n^2)$
* **Keep dominant term only**

---

## Step 5: Consider early returns (only if asked)

If code returns early sometimes:

* **Best case** might be smaller (often **O(1)**)
* **Worst case** still uses full loops

Exam default is **worst case** unless they ask best/average.

---

## Step 6: Space complexity (extra memory)

Ask: does extra memory grow with (n)?

* Only a few variables → **O(1)**
* New list/set/dict that grows with (n) → **O(n)**

---

# Worked Examples (copy these patterns)

## Example 1: Linear search

```python
for x in arr:
    if x == target:
        return True
return False
```

**Step-by-step**

1. $n = \text{len(arr)}$
2. basic op: `x == target`
3. loop runs up to (n) times
4. total ops ~ (n)
   ✅ **Time (worst): O(n)**
   ✅ **Space: O(1)**
   Best case: first element matches → **O(1)**

---

## Example 2: Your duplicates code (original)

```python
for i in range(n):
    for j in range(0, n):
        if i != j:
            if arr[i] == arr[j]:
                return True
return False
```

**Step-by-step**

1. $n = \text{len(arr)}$
2. basic op: `arr[i] == arr[j]`
3. outer loop: (n)
4. inner loop: (n)
5. nested → $n \times n = n^2$ comparisons (minus diagonal doesn’t change Big-O)
6. simplify: $n^2 - n \rightarrow O(n^2)$

✅ **Time (worst): O(n²)**
✅ **Space: O(1)**
Best case: duplicate found immediately → **O(1)**

---

## Example 3: Your duplicates code (optimized triangle)

```python
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            return True
return False
```

**Step-by-step**

1. $n = \text{len(arr)}$
2. basic op: `arr[i] == arr[j]`
3. outer: (n)
4. inner: runs fewer each time
   $$
   (n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2}
   $$
5. simplify: $\frac{1}{2}n^2 - \frac{1}{2}n \rightarrow O(n^2)$

✅ **Time (worst): O(n²)**
✅ **Space: O(1)**
Note: about half comparisons vs original, but still **O(n²)**.

---

## Example 4: Two separate loops (add, don’t multiply)

```python
for i in range(n):   # loop A
    ...

for j in range(n):   # loop B
    ...
```

Total work: ($n + n = 2n \rightarrow O(n)$)

✅ **Time: O(n)**

---

## Example 5: Using a set (faster time, more space)

```python
seen = set()
for x in arr:
    if x in seen:
        return True
    seen.add(x)
return False
```

**Step-by-step**

1. $n = \text{len(arr)}$
2. loop runs (n)
3. set lookup average (O(1))
4. total: $n \cdot 1 = O(n)$
   Space: `seen` can grow to size (n) → **O(n)**

✅ **Time (avg): O(n)**
✅ **Space: O(n)**

---

# Mini “Big-O Rules” box (perfect for cheat sheet)

* `for i in range(n)` → **O(n)**
* nested `for` over `n` → **O(n²)**
* `for j in range(i, n)` (triangle) → **O(n²)**
* two loops one after the other → **O(n)**
* drop constants: ($5n \rightarrow O(n)$)
* drop smaller terms: ($n^2 + n \rightarrow O(n^2)$)
* space: extra structure grows with (n) → **O(n)** else **O(1)**

## Linear Search (sequential scan)

### Pseudocode

```text
FUNCTION LinearSearch(A, target)
    // A is a list/array, unsorted is OK
    FOR i FROM 0 TO LENGTH(A) - 1 DO
        IF A[i] = target THEN
            RETURN i          // found at index i
        ENDIF
    ENDFOR
    RETURN -1                 // not found
ENDFUNCTION
```

### Big-O (time)

* **Best case:** **O(1)** (target is first element)
* **Average case:** **O(n)**
* **Worst case:** **O(n)** (target last or not present)

### Big-O (space)

* **O(1)**

### When to use

* List **not sorted**
* Small data or one-off search
* Works on arrays/lists/linked lists

---

## Binary Search (divide-and-conquer)

### Requirement

* **A must be sorted** (usually ascending)
* Works best when you have **fast indexing** (array/list)

### Pseudocode (iterative)

```text
FUNCTION BinarySearch(A, target)
    // A must be sorted ascending
    low ← 0
    high ← LENGTH(A) - 1

    WHILE low ≤ high DO
        mid ← (low + high) DIV 2

        IF A[mid] = target THEN
            RETURN mid
        ELSE IF A[mid] < target THEN
            low ← mid + 1
        ELSE
            high ← mid - 1
        ENDIF
    ENDWHILE

    RETURN -1
ENDFUNCTION
```

### Big-O (time)

* **Best case:** **O(1)** (mid is target immediately)
* **Average case:** **O(log n)**
* **Worst case:** **O(log n)**

### Big-O (space)

* Iterative: **O(1)**
* Recursive version: **O(log n)** (call stack)

### When to use

* Data is **sorted**
* You’ll do **lots of searches**
* Large datasets where speed matters

---

### One-line cheat sheet

* **Linear Search:** unsorted OK, **O(n)** worst
* **Binary Search:** must be sorted, **O(log n)** worst

