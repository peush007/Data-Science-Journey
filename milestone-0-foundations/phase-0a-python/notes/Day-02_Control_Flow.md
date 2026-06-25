# Day 02 — Control Flow (if / elif / else)

## What is Control Flow?

Control Flow is the mechanism that determines the order in which statements are executed in a program.

By default, Python executes code from top to bottom. Control Flow allows a program to make decisions and execute different blocks of code depending on conditions.

Think of it as the "decision-making system" of a program.

---

## Why Control Flow Matters in Data Science

Almost every Data Science application involves decision making.

Examples:

* Classifying customers into Silver, Gold, or Platinum categories
* Detecting fraudulent transactions
* Handling missing values in datasets
* Choosing different actions based on model predictions
* Filtering useful data from unwanted data

Without Control Flow, a program cannot make intelligent decisions.

---

## The 3 Core Decision Structures

| Structure        | Purpose                               | Example                            |
| ---------------- | ------------------------------------- | ---------------------------------- |
| if               | Execute code when a condition is True | Check if marks are greater than 50 |
| if / else        | Handle True and False outcomes        | Pass or Fail                       |
| if / elif / else | Handle multiple outcomes              | Grade System                       |

---

## The if Statement

The if statement checks a condition.

If the condition evaluates to True, Python executes the code inside the block.

If the condition is False, Python skips the block.

Example:

```python
marks = 85

if marks >= 50:
    print("Passed")
```

Output:

```text
Passed
```

---

## The if / else Statement

The else block executes when the if condition becomes False.

This allows a program to handle both possible outcomes.

Example:

```python
marks = 35

if marks >= 50:
    print("Passed")
else:
    print("Failed")
```

Output:

```text
Failed
```

---

## The if / elif / else Statement

When multiple conditions need to be checked, Python uses elif (Else If).

Python checks conditions from top to bottom.

The first condition that becomes True is executed.

All remaining conditions are skipped.

Example:

```python
marks = 72

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Grade F")
```

Output:

```text
Grade C
```

---

## Comparison Operators

Comparison operators are used to compare values.

| Operator | Meaning                  | Example |
| -------- | ------------------------ | ------- |
| ==       | Equal To                 | 5 == 5  |
| !=       | Not Equal To             | 5 != 3  |
| >        | Greater Than             | 10 > 5  |
| <        | Less Than                | 3 < 8   |
| >=       | Greater Than or Equal To | 5 >= 5  |
| <=       | Less Than or Equal To    | 4 <= 6  |

These operators always return either True or False.

---

## Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning                             | Example                  |
| -------- | ----------------------------------- | ------------------------ |
| and      | All conditions must be True         | age >= 18 and has_id     |
| or       | At least one condition must be True | is_student or is_teacher |
| not      | Reverses the condition              | not is_banned            |

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
```

Output:

```text
Entry Allowed
```

---

## Nested if Statements

A Nested if statement is an if statement inside another if statement.

It is used when one condition should be checked only after another condition becomes True.

Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
```

Output:

```text
Entry Allowed
```

---

## Real Data Science Applications

| Application            | Use of Control Flow              |
| ---------------------- | -------------------------------- |
| Customer Segmentation  | Classify customers into groups   |
| Fraud Detection        | Flag suspicious transactions     |
| Recommendation Systems | Suggest products or movies       |
| Data Validation        | Detect missing or invalid values |
| Loan Approval Systems  | Approve or reject applications   |

---

## Common Mistakes

### Using = instead of ==

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

### Forgetting Colon

Wrong:

```python
if marks >= 50
```

Correct:

```python
if marks >= 50:
```

### Wrong Indentation

Wrong:

```python
if marks >= 50:
print("Passed")
```

Correct:

```python
if marks >= 50:
    print("Passed")
```

### Incorrect Condition Order

Wrong:

```python
if marks >= 50:
    print("D")

elif marks >= 90:
    print("A")
```

Correct:

```python
if marks >= 90:
    print("A")

elif marks >= 50:
    print("D")
```

---

## Interview Questions

Q: What is Control Flow in Python?

A: Control Flow determines the order in which program statements execute based on conditions and decisions.

Q: What is the difference between if and if/else?

A: if handles one outcome, while if/else handles both True and False outcomes.

Q: What is elif?

A: elif stands for "Else If" and is used to check multiple conditions.

Q: Is else mandatory?

A: No. else is optional in Python.

Q: What happens if multiple elif conditions are True?

A: Python executes only the first True condition and skips the remaining conditions.

---

## Key Takeaway

Control Flow is the decision-making engine of every program.

Using if, if/else, and if/elif/else, Python can evaluate conditions and choose different execution paths.

From customer segmentation to fraud detection and recommendation systems, Control Flow is used everywhere in Data Science and Machine Learning.
