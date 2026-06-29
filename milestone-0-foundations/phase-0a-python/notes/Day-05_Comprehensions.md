# Day 05 — List & Dictionary Comprehensions

## What is a Comprehension?

A comprehension is a short, clean way to create a new list or dictionary from an existing collection — all in one single line.

Think of it like this:

* Without comprehension — you pick up each fruit one by one, check if it is fresh, and if yes put it in the new basket. That is a regular loop.
* With comprehension — you describe what you want in one instruction: "new basket of all fresh fruits from old basket." Python does the rest automatically.

Python has two types of comprehensions that every Data Scientist uses daily.

---

## Why Comprehensions Matter in Data Science

In Data Science you constantly transform data. Take a list of raw values and create a new cleaned list from it. Take a list of column names and create a dictionary mapping each column to its data type. Filter out invalid values from a dataset column.

Examples:

* Without comprehensions you write 4-5 lines of loop code every time
* With comprehensions you do the same thing in one clean, readable line
* Comprehensions are faster than regular loops because Python optimizes them internally
* Every professional Data Science codebase uses comprehensions heavily

Without comprehensions you cannot read real production code. Libraries like Pandas, Scikit-Learn, and NumPy use comprehension logic internally.

---

## The 2 Core Comprehension Types

| Type                     | Output     | Syntax                                          |
| ------------------------ | ---------- | ----------------------------------------------- |
| List Comprehension       | List [ ]   | [expression for item in collection]             |
| Dictionary Comprehension | Dict { }   | {key: value for item in collection}             |

---

## List Comprehensions

A list comprehension creates a new list by applying an expression to every item in an existing collection.

Basic Syntax:

```python
new_list = [expression for item in collection]
```

Read it like this: "Give me expression, for every item in collection."

---

## Without vs With Comprehension

Without comprehension — regular loop:

```python
marks = [85, 92, 78, 65, 90]
doubled = []

for mark in marks:
    doubled.append(mark * 2)

print(doubled)
```

Output:

```text
[170, 184, 156, 130, 180]
```

With comprehension — one line:

```python
marks = [85, 92, 78, 65, 90]
doubled = [mark * 2 for mark in marks]
print(doubled)
```

Output:

```text
[170, 184, 156, 130, 180]
```

Exact same result. One line instead of four. Cleaner. Faster. More professional.

---

## Real Data Science Use of List Comprehensions

Example:

```python
columns = ["Age", "Salary", "DEPARTMENT", "City"]
clean_columns = [col.lower() for col in columns]
print(clean_columns)
```

Output:

```text
['age', 'salary', 'department', 'city']
```

This is one of the most common data cleaning operations in Data Science. Raw datasets often have inconsistent column name casing. This one line fixes all of them instantly.

---

## List Comprehensions with Conditions

You can add an if condition to filter items. Only items where the condition is True get included in the new list.

Syntax with Condition:

```python
new_list = [expression for item in collection if condition]
```

---

## Filtering with List Comprehensions

Example — Remove missing values from dataset column:

```python
ages = [25, None, 30, None, 28, 35, None, 22]
clean_ages = [age for age in ages if age is not None]
print(clean_ages)
```

Output:

```text
[25, 30, 28, 35, 22]
```

This is real data cleaning. Every Data Scientist removes None values from columns constantly. This one line does it cleanly and efficiently.

---

## Comprehension with if/else — Transformation

When you want to transform every item — not filter — you put the if/else before the for.

Syntax:

```python
new_list = [value_if_true if condition else value_if_false for item in collection]
```

Example — label every mark as Pass or Fail:

```python
marks = [85, 42, 92, 38, 78]
labels = ["Pass" if mark >= 50 else "Fail" for mark in marks]
print(labels)
```

Output:

```text
['Pass', 'Fail', 'Pass', 'Fail', 'Pass']
```

This is exactly how you create a target label column in a dataset — one of the most fundamental operations in Machine Learning data preparation.

---

## Dictionary Comprehensions

A dictionary comprehension creates a new dictionary from an existing collection in one line.

Basic Syntax:

```python
new_dict = {key_expression: value_expression for item in collection}
```

---

## Real Data Science Use of Dictionary Comprehensions

Example — Storing model results:

```python
models = ["LinearRegression", "RandomForest", "XGBoost"]
scores = [0.82, 0.91, 0.94]

model_results = {model: score for model, score in zip(models, scores)}
print(model_results)
```

Output:

```text
{'LinearRegression': 0.82, 'RandomForest': 0.91, 'XGBoost': 0.94}
```

This exact pattern is used when comparing multiple ML models and storing their performance scores in one clean dictionary.

---

## Dictionary Comprehension with Condition

Example — Filter only high performing models:

```python
model_results = {
    "LinearRegression": 0.82,
    "RandomForest": 0.91,
    "XGBoost": 0.94,
    "SVM": 0.78
}

good_models = {model: score for model, score in model_results.items() if score >= 0.90}
print(good_models)
```

Output:

```text
{'RandomForest': 0.91, 'XGBoost': 0.94}
```

Filtering only models that meet a performance threshold. This is real model selection logic used in production ML pipelines.

---

## When to Use Comprehensions vs Loops

| Situation                                   | Use                |
| ------------------------------------------- | ------------------ |
| Simple transformation of a collection       | Comprehension      |
| Simple filtering of a collection            | Comprehension      |
| Complex multi-step logic                    | Regular loop       |
| More than 2 conditions                      | Regular loop       |
| Need to track state across iterations       | Regular loop       |
| Code needs to be read by beginners          | Regular loop       |

---

## Real Data Science Applications

| Application                        | Comprehension Used                              |
| ---------------------------------- | ----------------------------------------------- |
| Clean column names to lowercase    | List Comprehension                              |
| Remove None values from column     | List Comprehension with condition               |
| Create Pass/Fail label column      | List Comprehension with if/else                 |
| Map column names to data types     | Dictionary Comprehension                        |
| Store model names to scores        | Dictionary Comprehension                        |
| Filter models by accuracy threshold| Dictionary Comprehension with condition         |

---

## Interview Questions

Q: What is a list comprehension?

A: A list comprehension is a concise one-line syntax to create a new list by applying an expression to every item in an existing collection, with an optional condition to filter items.

Q: What is the syntax of a list comprehension?

A: [expression for item in collection] — or with condition: [expression for item in collection if condition]

Q: What is the difference between a list comprehension with if only vs if/else?

A: If only — placed after the for — filters items, only including items where condition is True. If/else — placed before the for — transforms every item, giving one value if True and another if False. No items are excluded.

Q: Are comprehensions faster than loops?

A: Yes. Python optimizes comprehensions internally making them generally faster than equivalent for loops, especially for large collections.

Q: What is a dictionary comprehension?

A: A concise one-line syntax to create a new dictionary from a collection. Syntax: {key: value for item in collection}

Q: Where are comprehensions used in Data Science?

A: Cleaning column names, removing missing values, transforming values, creating label columns, mapping model names to scores, filtering dataset values based on conditions — essentially anywhere you transform or filter a collection.

---

## Key Takeaway

Comprehensions are the mark of professional Python code.

Every real Data Science codebase uses them. They make data transformation and cleaning faster, cleaner, and more readable when used correctly.

A Data Scientist who writes comprehensions thinks in collections — which is exactly how Data Science works. You never process one value. You always process an entire column, an entire dataset, an entire collection.