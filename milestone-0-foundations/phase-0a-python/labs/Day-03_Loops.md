# Day 03 — Labs
📅 Date: 26 June 2026
🎯 Milestone 0 — Phase 0A: Python Mastery
💻 Topic: Loops — for loop and while loop
⚙️ Environment: VS Code — Python

---

## Lab 1 — Basic for Loop

Code:
students = ["Rahul", "Priya", "Amit", "Sara"]
for student in students:
    print("Hello", student)

Output:
Hello Rahul
Hello Priya
Hello Amit
Hello Sara

What this shows:
for loop goes through every item in the list.
Each item is stored in student one at a time.
Print runs once for every item automatically.

---

## Lab 2 — range() with for Loop

Code:
for i in range(1, 6):
    print("Row number:", i)

Output:
Row number: 1
Row number: 2
Row number: 3
Row number: 4
Row number: 5

What this shows:
range(1, 6) generates numbers 1 to 5.
Loop runs exactly 5 times automatically.
Used in Data Science to process fixed number of iterations.

---

## Lab 3 — while Loop

Code:
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

Output:
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

What this shows:
while checks condition before every iteration.
count += 1 prevents infinite loop.
Loop stops when count becomes 6.

---

## Lab 4 — break Statement

Code:
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    if number == 30:
        break
    print(number)

Output:
10
20

What this shows:
Loop stops completely when number equals 30.
Everything after 30 is never processed.

---

## Lab 5 — continue Statement

Code:
data = [100, 250, None, 400, None, 600]
for value in data:
    if value is None:
        continue
    print("Processing:", value)

Output:
Processing: 100
Processing: 250
Processing: 400
Processing: 600

What this shows:
None values are skipped completely.
This is real Data Science missing value handling.
continue moves to next item without stopping loop.

---

## Lab 6 — ML Training Loop (Real DS Use Case)

Code:
model_accuracy = 0.60
target_accuracy = 0.90

while model_accuracy < target_accuracy:
    print("Training... accuracy:", model_accuracy)
    model_accuracy += 0.05

print("Target reached:", round(model_accuracy, 2))

Output:
Training... accuracy: 0.6
Training... accuracy: 0.65
Training... accuracy: 0.7
Training... accuracy: 0.75
Training... accuracy: 0.8
Training... accuracy: 0.85
Target reached: 0.9

What this shows:
This is exactly how ML training loops work.
Keep training until accuracy target is reached.
while loop perfect for unknown number of iterations.