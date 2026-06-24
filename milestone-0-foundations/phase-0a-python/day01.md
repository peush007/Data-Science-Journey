# Day 01 — Variables & Data Types

## What is a Variable?
A variable is a named storage location in memory that holds a value.
Think of it as a labelled box — the label is the variable name,
the content inside is the value.

---

## The 4 Core Data Types

| Data Type | Keyword | Example | Use in Data Science |
|-----------|---------|---------|-------------------|
| Text | str | "Rahul" | Column names, labels, categories |
| Whole Number | int | 21 | Row counts, years, rankings |
| Decimal Number | float | 8.5 | Accuracy scores, prices, measurements |
| Yes/No | bool | True | Flags, predictions, conditions |

---

## How to Create a Variable
variable_name = value
The = sign means "store this value" — NOT "equal to" like in maths.

---

## How to Check Data Type
Use the type() function:
type(variable_name)

---

## Variable Naming Rules
- Use letters, numbers, underscore only
- Cannot start with a number
- Case sensitive (age and Age are different)
- Cannot use Python keywords (if, for, True etc.)
- Always use meaningful names

---

## Common Mistakes
- Using hyphen instead of underscore: student-name WRONG
- Forgetting quotes around strings: city = Mumbai WRONG
- Starting with a number: 1st_score WRONG

---

## Interview Questions
Q: What is a variable in Python?
A: A named storage location in memory that holds a value, created using =

Q: Difference between int and float?
A: int = whole numbers (5, 100), float = decimal numbers (5.0, 99.9)

Q: Is Python case-sensitive for variable names?
A: Yes. name, Name, and NAME are three different variables.

---

## Key Takeaway
Variables are the foundation of every program.
Every dataset column, every model score, every prediction
starts with a variable.