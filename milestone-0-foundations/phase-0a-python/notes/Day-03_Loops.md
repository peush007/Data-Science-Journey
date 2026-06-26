# Day 03 — Loops (for loop & while loop)

## Why This Topic Exists in Data Science

Imagine you have a dataset with **1 million rows**. You need to check every single row for missing values. Are you going to write **1 million lines of code?** No. You write one loop and let it run **1 million times automatically.**

This is exactly why loops exist — to automate repetition. In Data Science, loops are everywhere:

* Processing every row in a dataset
* Training a model over multiple iterations (called epochs)
* Calculating statistics for every column
* Cleaning every value in a list
* Sending API requests for every item in a list

Without loops, Data Science at scale is impossible.

---

## What is a Loop?

A loop is a way to execute the same block of code multiple times without writing it multiple times.

Real world analogy: Imagine a teacher checking 40 student papers. She does not have a different process for each student. She follows the same process — pick paper, check answers, give marks, put it down — 40 times. That repeated process is a loop.

In Python there are two types of loops:

| Loop           | Purpose                                              |
| -------------- | ---------------------------------------------------- |
| **for loop**   | Used when you know exactly how many times to repeat  |
| **while loop** | Used when you repeat until a condition becomes False |

---

## The for Loop

The for loop repeats a block of code for every item in a sequence.

### Syntax

```python
for variable in sequence:
    # code to repeat
```

### Simple Example

```python
students = ["Rahul", "Priya", "Amit", "Sara"]

for student in students:
    print("Hello", student)
```

### Output

```text
Hello Rahul
Hello Priya
Hello Amit
Hello Sara
```

### Explanation

Python went through the list one item at a time. For each item it stored the value in the variable **student** and ran the print statement. It repeated until every item was processed.

### Real World Data Science Use

```python
columns = ["age", "salary", "experience", "score"]

for column in columns:
    print("Processing column:", column)
```

This is exactly how data preprocessing pipelines process every column in a dataset automatically.

---

## The range() Function

`range()` generates a sequence of numbers. It is used with for loops when you want to repeat something a specific number of times.

### Syntax

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1 with step
```

### Example 1

```python
# Print numbers 0 to 4
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

### Example 2

```python
# Print numbers 1 to 5
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

### Example 3

```python
# Print even numbers 0 to 8
for i in range(0, 10, 2):
    print(i)
```

### Output

```text
0
2
4
6
8
```

### Real World Data Science Use

Training a neural network for 100 epochs:

```python
for epoch in range(100):
    print("Training epoch:", epoch)
```

## The while Loop

The while loop keeps running as long as a condition is True. The moment the condition becomes False, the loop stops.

### Syntax

```python
while condition:
    # code to repeat
```

### Example

```python
count = 1

while count <= 5:
    print("Count:", count)
    count = count + 1
```

### Output

```text
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

### Explanation

Python checked — is `count <= 5`?

Yes.

It ran the block.

Added **1** to `count`.

Checked again.

Repeated until **count became 6** and the condition became False.

### Important Note

Always make sure the condition eventually becomes False.
If it never does, your loop runs forever — this is called an **Infinite Loop** and it will crash your program.

### Real World Data Science Use

```python
model_accuracy = 0.60
target_accuracy = 0.90

while model_accuracy < target_accuracy:
    print("Training... current accuracy:", model_accuracy)
    model_accuracy += 0.05

print("Target reached:", model_accuracy)
```

This is exactly how ML training loops work — keep training until accuracy target is reached.

---

## break and continue

### break

The **break** statement stops the loop completely and exits it immediately.

### Example

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        break
    print(number)
```

### Output

```text
10
20
```

Loop stopped the moment it hit **30**.

---

### continue

The **continue** statement skips the current iteration and moves to the next one.

### Example

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        continue
    print(number)
```

### Output

```text
10
20
40
50
```

30 was skipped.

Everything else printed normally.

### Real World Data Science Use

```python
data = [100, 250, None, 400, None, 600]

for value in data:
    if value is None:
        continue
    print("Processing value:", value)
```

This is exactly how you skip missing values (`None`) in a dataset while processing.

---

## Nested Loops

A loop inside another loop. The inner loop completes fully for every single iteration of the outer loop.

### Example

```python
teams = ["Team A", "Team B"]
members = ["Alice", "Bob", "Charlie"]

for team in teams:
    for member in members:
        print(team, "—", member)
```

### Output

```text
Team A — Alice
Team A — Bob
Team A — Charlie
Team B — Alice
Team B — Bob
Team B — Charlie
```

### Real World Data Science Use

Nested loops are used when working with:

- Matrices
- 2D arrays
- Grid searches in Machine Learning
- Testing every combination of hyperparameters

---

## for Loop vs while Loop

| for loop | while loop |
|-----------|------------|
| Used when you know exactly how many times to repeat | Used when you repeat until a condition becomes False |
| Best for sequences like lists, tuples, strings, and range() | Best when repetition depends on a condition |
| Stops automatically after the sequence ends | Stops only when the condition becomes False |
| Less chance of creating an infinite loop | Higher chance of creating an infinite loop |

---

## Interview Questions

**Q: What is a loop in Python?**

**A:** A loop is a way to execute the same block of code multiple times without writing it multiple times.

---

**Q: What is the difference between a for loop and a while loop?**

**A:** A `for` loop is used when you know exactly how many times to repeat, while a `while` loop is used when repetition depends on a condition becoming False.

---

**Q: What is range()?**

**A:** `range()` generates a sequence of numbers and is commonly used with `for` loops.

---

**Q: What does break do?**

**A:** `break` immediately stops the loop and exits it.

---

**Q: What does continue do?**

**A:** `continue` skips the current iteration and moves to the next iteration.

---

**Q: What is a nested loop?**

**A:** A nested loop is a loop inside another loop. The inner loop executes completely for every iteration of the outer loop.

---

## Key Takeaway

Loops automate repetition.

Instead of writing the same code multiple times, Python can repeat it automatically using loops.

The `for` loop is best when the number of repetitions is known.

The `while` loop is best when repetition depends on a condition.

From data cleaning to Machine Learning training, loops are one of the most important concepts in Data Science.