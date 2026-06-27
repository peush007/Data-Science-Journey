

## Lab 1 — Lists

marks = [85, 92, 78, 65, 90]

print(marks[0])
print(marks[-1])
print(marks[1:4])
print(len(marks))
print(max(marks))
print(min(marks))

Output:
85
90
[92, 78, 65]
5
92
65

What this shows:
List indexing, slicing, and built-in
functions working on a collection of values.

---

## Lab 2 — List Methods

marks = [85, 92, 78]

marks.append(95)
print(marks)

marks.sort()
print(marks)

marks.remove(78)
print(marks)

Output:
[85, 92, 78, 95]
[78, 85, 92, 95]
[85, 92, 95]

What this shows:
append adds to end, sort orders ascending,
remove deletes first occurrence of value.

---

## Lab 3 — Model Accuracy Tracker

accuracies = [0.82, 0.87, 0.91, 0.89, 0.94]

print("Best:", max(accuracies))
print("Worst:", min(accuracies))
print("Average:", sum(accuracies) / len(accuracies))

Output:
Best: 0.94
Worst: 0.82
Average: 0.886

What this shows:
Exact pattern used to track and compare
model performance across experiments.

---

## Lab 4 — Tuples

coordinates = (19.0760, 72.8777)
config = ("random_forest", 100, 42)

print(coordinates[0])
print(config[0])

Output:
19.076
random_forest

What this shows:
Tuples store fixed data that should never
change — coordinates, model configuration.

---

## Lab 5 — Dictionaries

model_results = {
    "accuracy": 0.94,
    "precision": 0.91,
    "recall": 0.89,
    "f1_score": 0.90
}

print(model_results["accuracy"])
print(model_results.keys())
print(model_results.values())

Output:
0.94
dict_keys(['accuracy', 'precision', 'recall', 'f1_score'])
dict_values([0.94, 0.91, 0.89, 0.9])

What this shows:
Storing and accessing model metrics using
dictionary — most common DS pattern.

---

## Lab 6 — Sets — Finding Unique Categories

categories = ["Electronics", "Clothing", "Food",
              "Electronics", "Food", "Books"]

unique = set(categories)
print(unique)
print("Total unique:", len(unique))

Output:
{'Electronics', 'Clothing', 'Food', 'Books'}
Total unique: 4

What this shows:
set() removes duplicates automatically.
Same logic Pandas .unique() uses internally.

---

## Lab 7 — Set Operations

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)

Output:
{1, 2, 3, 4, 5, 6, 7, 8}
{4, 5}
{1, 2, 3}

What this shows:
Union, intersection, difference —
fundamental set operations used in
data comparison and deduplication tasks.