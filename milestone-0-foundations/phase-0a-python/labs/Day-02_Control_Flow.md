# Day 02 — Labs
📅 Date: 25 June 2026
🎯 Milestone 0 — Phase 0A: Python Mastery
💻 Topic: Control Flow — if / elif / else
⚙️ Environment: VS Code — Python

---

## Lab 1 — Basic if Statement

Code:
marks = 85

if marks >= 50:
    print("You passed!")

Output:
You passed!

What this shows:
Python checks the condition marks >= 50.
85 is greater than 50 so condition is True.
Print statement runs.
If marks was 40 nothing would print.

---

## Lab 2 — if/else Statement

Code:
marks = 35

if marks >= 50:
    print("You passed!")
else:
    print("You failed. Try again.")

Output:
You failed. Try again.

What this shows:
marks is 35 which is less than 50.
Condition is False so else block runs.
Only one block ever runs — either if or else.

---

## Lab 3 — if/elif/else — Grade System

Code:
marks = 72

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F — Failed")

Output:
Grade: C

What this shows:
Python checks from top to bottom.
marks >= 90 — False, skip.
marks >= 75 — False, skip.
marks >= 60 — True, run this block.
Remaining conditions skipped completely.

---

## Lab 4 — Logical Operators

Code:
python_score = 85
math_score = 78
has_degree = True

if python_score >= 80 and math_score >= 70 and has_degree == True:
    print("Eligible for Data Science role")
else:
    print("Not eligible yet")

Output:
Eligible for Data Science role

What this shows:
All three conditions must be True for and to pass.
85 >= 80 True.
78 >= 70 True.
has_degree == True True.
All True so if block runs.

---

## Lab 5 — Customer Segmentation (Real DS Use Case)

Code:
purchase_amount = 4500

if purchase_amount >= 10000:
    customer_type = "Platinum"
elif purchase_amount >= 5000:
    customer_type = "Gold"
elif purchase_amount >= 1000:
    customer_type = "Silver"
else:
    customer_type = "Basic"

print("Customer Type:", customer_type)

Output:
Customer Type: Silver

What this shows:
This is real Data Science logic.
Categorizing customers based on purchase value.
This exact pattern is used in e-commerce
customer segmentation pipelines.

---

## Lab 6 — Nested if Statements

Code:
age = 20
has_id = True

if age >= 18:
    if has_id == True:
        print("Entry allowed")
    else:
        print("Need ID to enter")
else:
    print("Too young to enter")

Output:
Entry allowed

What this shows:
First checks age condition.
If age passes then checks ID condition.
Both must pass for entry allowed to print.
This is nested decision making.