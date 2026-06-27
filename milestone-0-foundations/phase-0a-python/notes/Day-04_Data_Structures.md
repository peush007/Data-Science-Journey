# Day 04 — Data Structures (Lists, Tuples, Dictionaries, Sets)

## What is a Data Structure?

A data structure is a way of organizing and storing multiple values together so they can be accessed and manipulated efficiently.

Think of four different ways to store items:

* A shopping list on paper — ordered, you can add/remove items — that is a List
* A sealed envelope with fixed documents inside — ordered, cannot change — that is a Tuple
* A contact book with name mapped to phone number — key-value pairs — that is a Dictionary
* A bag of unique lottery tickets — no duplicates, no order — that is a Set

Python has four built-in data structures that every Data Scientist uses daily.

---

## Why Data Structures Matter in Data Science

Every single day in Data Science you work with collections of data. Not one value — thousands of values together.

Examples:

* A column of 1000 customer names is a list
* A row of fixed attributes about one customer is a tuple
* A dictionary of feature names mapped to their values is exactly what a Python dictionary is
* A collection of unique categories in a dataset is a set

Without data structures you cannot handle real world data. Pandas DataFrames are built on top of these exact structures internally. NumPy arrays are an advanced form of lists. Every ML model takes lists or arrays as input.

---

## The 4 Core Data Structures

| Structure  | Ordered | Changeable | Duplicates | Brackets |
| ---------- | ------- | ---------- | ---------- | -------- |
| List       | Yes     | Yes        | Yes        | [ ]      |
| Tuple      | Yes     | No         | Yes        | ( )      |
| Dictionary | No      | Yes        | Keys: No   | { }      |
| Set        | No      | Yes        | No         | { }      |

---

## Lists

A list is an ordered, changeable collection that allows duplicate values. It is the most commonly used data structure in Python.

Example:

```python
marks = [85, 92, 78, 65, 90]
names = ["Rahul", "Priya", "Arjun"]
```

---

## Accessing List Items — Indexing

Python indexing starts at 0 not 1. The first item is always index 0. Negative indexing counts from the end. -1 is always the last item.

Example:

```python
marks = [85, 92, 78, 65, 90]

print(marks[0])   # First item
print(marks[1])   # Second item
print(marks[-1])  # Last item
print(marks[-2])  # Second last
```

Output:

```text
85
92
90
65
```

---

## List Slicing

Example:

```python
marks = [85, 92, 78, 65, 90]

print(marks[1:4])   # Items from index 1 to 3
print(marks[:3])    # First 3 items
print(marks[2:])    # From index 2 to end
```

Output:

```text
[92, 78, 65]
[85, 92, 78]
[78, 65, 90]
```

---

## Most Important List Methods

Example:

```python
marks = [85, 92, 78]

marks.append(95)        # Add item to end
marks.insert(1, 100)    # Insert at index 1
marks.remove(78)        # Remove first occurrence of 78
marks.pop()             # Remove and return last item
marks.sort()            # Sort in ascending order

print(len(marks))       # Number of items
print(max(marks))       # Highest value
print(min(marks))       # Lowest value
print(sum(marks))       # Sum of all values
```

---

## Real Data Science Use of Lists

Example:

```python
accuracies = [0.82, 0.87, 0.91, 0.89, 0.94]

print("Best accuracy:", max(accuracies))
print("Average accuracy:", sum(accuracies) / len(accuracies))
```

Output:

```text
Best accuracy: 0.94
Average accuracy: 0.886
```

This is exactly how Data Scientists track and compare model performance across multiple experiments.

---

## Tuples

A tuple is an ordered, unchangeable collection that allows duplicate values. Once created, you cannot modify it.

Example:

```python
coordinates = (19.0760, 72.8777)    # Mumbai lat/long
rgb_color = (255, 128, 0)
student = ("Rahul", 21, "Mumbai")
single = (42,)                       # Single item tuple needs comma
```

The comma after a single item is mandatory — without it Python treats it as just a value in brackets, not a tuple.

---

## List vs Tuple

| Feature    | List       | Tuple         |
| ---------- | ---------- | ------------- |
| Brackets   | [ ]        | ( )           |
| Changeable | Yes        | No            |
| Use when   | Data changes | Data is fixed |
| Speed      | Slower     | Faster        |
| DS Use     | Dataset values, results | Coordinates, config, fixed records |

---

## Real Data Science Use of Tuples

Example:

```python
# Geographic coordinates should never change
mumbai = (19.0760, 72.8777)
delhi = (28.7041, 77.1025)

# Model configuration — should not change during training
config = ("random_forest", 100, 42)   # model name, n_estimators, random_state
```

---

## Dictionaries

A dictionary stores data as key-value pairs. Instead of accessing data by index number, you access it by a meaningful key name.

Example:

```python
student = {
    "name": "Rahul",
    "age": 21,
    "gpa": 8.5,
    "city": "Mumbai"
}
```

Dictionaries use curly brackets { }. Each item is a key-value pair separated by colon. Keys must be unique. Values can be any data type.

---

## Accessing and Updating Dictionary Values

Example:

```python
student = {"name": "Rahul", "age": 21, "gpa": 8.5}

print(student["name"])     # Rahul
print(student["age"])      # 21

student["city"] = "Mumbai"      # Add new key
student["age"] = 22             # Update existing key
```

---

## Most Important Dictionary Methods

Example:

```python
student = {"name": "Rahul", "age": 21, "gpa": 8.5}

print(student.keys())      # All keys
print(student.values())    # All values
print(student.items())     # All key-value pairs

student.pop("gpa")         # Remove a key
```

Output:

```text
dict_keys(['name', 'age', 'gpa'])
dict_values(['Rahul', 21, 8.5])
dict_items([('name', 'Rahul'), ('age', 21), ('gpa', 8.5)])
```

---

## Real Data Science Use of Dictionaries

Example:

```python
model_results = {
    "accuracy": 0.94,
    "precision": 0.91,
    "recall": 0.89,
    "f1_score": 0.90
}

print("Model Accuracy:", model_results["accuracy"])
print("F1 Score:", model_results["f1_score"])
```

Output:

```text
Model Accuracy: 0.94
F1 Score: 0.90
```

Pandas .dtypes which you will use constantly in Data Science returns data in dictionary format. JSON data from APIs is also dictionary format.

---

## Sets

A set is an unordered collection of unique values. It automatically removes duplicates. Order is not guaranteed.

Example:

```python
categories = {"Electronics", "Clothing", "Food", "Electronics"}
print(categories)
```

Output:

```text
{'Electronics', 'Clothing', 'Food'}
```

The duplicate "Electronics" was automatically removed.

---

## Most Important Set Operations

Example:

```python
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a | set_b)    # Union — all items from both
print(set_a & set_b)    # Intersection — items in both
print(set_a - set_b)    # Difference — items in A not in B
```

Output:

```text
{1, 2, 3, 4, 5, 6, 7, 8}
{4, 5}
{1, 2, 3}
```

---

## Real Data Science Use of Sets

Example:

```python
product_categories = ["Electronics", "Clothing", "Food",
                      "Electronics", "Food", "Clothing", "Books"]

unique_categories = set(product_categories)
print("Unique categories:", unique_categories)
print("Total unique:", len(unique_categories))
```

Output:

```text
Unique categories: {'Electronics', 'Clothing', 'Food', 'Books'}
Total unique: 4
```

This is exactly what Pandas .unique() and .nunique() do internally — they use set logic to find unique values in a column.

---

## Choosing the Right Data Structure

| Situation                              | Use        |
| -------------------------------------- | ---------- |
| Ordered collection that changes        | List       |
| Ordered collection that never changes  | Tuple      |
| Key-value mapping, lookup by name      | Dictionary |
| Unique values, remove duplicates       | Set        |
| Dataset column values                  | List       |
| Model configuration                    | Tuple      |
| Model metrics and results              | Dictionary |
| Unique categories in a column          | Set        |

---

## Real Data Science Applications

| Application            | Data Structure Used                        |
| ---------------------- | ------------------------------------------ |
| Dataset column values  | List                                       |
| Model configuration    | Tuple                                      |
| Model metrics / JSON   | Dictionary                                 |
| Unique categories      | Set                                        |
| Pandas DataFrames      | Built on Lists and Dictionaries internally |
| NumPy arrays           | Advanced form of Lists                     |

---

## Interview Questions

Q: What is the difference between a List and a Tuple?

A: Both are ordered collections. A list is mutable — you can add, remove, and change items. A tuple is immutable — once created it cannot be changed. Use lists for data that changes, tuples for data that must remain fixed.

Q: What is the difference between a List and a Set?

A: A list is ordered and allows duplicates. A set is unordered and only stores unique values — duplicates are automatically removed.

Q: How do you access a value in a dictionary?

A: By using its key inside square brackets — dictionary["key"] — or using .get("key") which returns None if key does not exist instead of raising an error.

Q: Can a dictionary have duplicate keys?

A: No. Keys must be unique. If you assign a value to an existing key, it overwrites the previous value.

Q: Why are data structures important in Data Science?

A: All data in Data Science is stored in collections. Lists store column values, dictionaries store model metrics and JSON data, sets find unique categories, tuples store fixed configurations. Pandas and NumPy are built on these structures internally.

Q: What does indexing start at in Python?

A: 0. The first item is always at index 0, not index 1.

---

## Key Takeaway

Data structures are how you organize information before analyzing it.

A Data Scientist who does not understand lists, tuples, dictionaries, and sets will struggle with every library they touch — because NumPy, Pandas, Scikit-Learn, and every other DS library is built on these foundations.

Master these four structures and you have mastered the container logic of all of Data Science.