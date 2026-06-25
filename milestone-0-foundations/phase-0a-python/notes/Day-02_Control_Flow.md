🎯 Topic: Control Flow — if / elif / else
📖 WHY THIS TOPIC EXISTS IN DATA SCIENCE

💡 Every intelligent decision a computer makes comes down to one thing — checking a condition and choosing what to do next. This is called Control Flow.

🎬 Think about this: when Netflix recommends you a movie, it is checking — did you watch thrillers before? If yes, recommend a thriller. If no, recommend something else. That decision logic is built on if/elif/else.

🔹 In Data Science specifically, control flow is used everywhere:

✅ Classifying data into categories

✅ Checking if a value is missing or present

✅ Deciding which model to use based on data size

✅ Flagging suspicious values in a dataset

✅ Every single ML prediction at its core is a condition check

🚀 Without understanding control flow, you cannot write a single meaningful Data Science program. It is the decision engine of every intelligent system.

🔵 Subtopic 1 — What is Control Flow?

📌 By default Python runs code line by line from top to bottom. Control flow means you can change that direction based on conditions.

🚉 Real world analogy:

Imagine you are at a railway station. There is a sign that says:

➡️ If your train is on Platform 1 — go left

➡️ Else if your train is on Platform 2 — go right

➡️ Else — check the board again

Your movement depends on a condition. That is exactly what control flow does in code.

🟢 Subtopic 2 — The if Statement

📌 The simplest form of control flow. Check one condition. If it is True, execute the code inside.

🔹 Syntax
if condition:
    # code runs only if condition is True

⚠️ The colon : at the end of the if line is mandatory.

⚠️ The code inside must be indented (4 spaces or 1 Tab).

Python uses indentation to know what belongs inside the if block.

🔹 Example
marks = 85

if marks >= 50:
    print("You passed!")
✅ Output
You passed!

📖 What happened: Python checked — is 85 greater than or equal to 50? Yes. So it ran the print statement.

If marks was 40, nothing would print because the condition would be False.

🟡 Subtopic 3 — The if/else Statement

📌 What if you want something to happen when the condition is False too? That is where else comes in.

🔹 Syntax
if condition:
    # runs if condition is True
else:
    # runs if condition is False
🔹 Example
marks = 35

if marks >= 50:
    print("You passed!")
else:
    print("You failed. Try again.")
✅ Output
You failed. Try again.
🏦 Real world Data Science use: Classifying a loan application.
credit_score = 620

if credit_score >= 700:
    print("Loan Approved")
else:
    print("Loan Rejected")

This exact logic runs inside every bank's loan approval system.

🟣 Subtopic 4 — The if/elif/else Statement

📌 What if you have more than two possible outcomes?

You use elif — which means "else if."

🔹 Syntax
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False AND condition2 is True
elif condition3:
    # runs if condition1 and condition2 are False AND condition3 is True
else:
    # runs if ALL conditions above are False

⚠️ Python checks conditions from top to bottom.

⚠️ The moment one condition is True, it runs that block and skips all remaining conditions.

🔹 Example
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
✅ Output
Grade: C
🛒 Real world Data Science use: Categorizing customers by purchase amount.
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
✅ Output
Customer Type: Silver

This exact logic is used in e-commerce platforms like Amazon and Flipkart to segment customers into loyalty tiers.

🔴 Subtopic 5 — Comparison Operators

📌 These are the tools you use inside conditions to compare values.

Operator	Meaning	Example	Result
==	Equal to	5 == 5	True
!=	Not equal to	5 != 3	True
>	Greater than	10 > 5	True
<	Less than	3 < 8	True
>=	Greater than or equal	5 >= 5	True
<=	Less than or equal	4 <= 6	True
⚠️ Very Important
age = 18          # = assigns value to variable
if age == 18:     # == checks if age equals 18
    print("You are exactly 18")

🚨 Beginners mix these up constantly.

🟠 Subtopic 6 — Logical Operators (Combining Conditions)

📌 Sometimes you need to check multiple conditions together.

Operator	Meaning	Example
and	Both conditions must be True	age > 18 and has_id == True
or	At least one condition must be True	is_student or is_teacher
not	Reverses the condition	not is_banned
💼 Real world example — checking eligibility for a Data Science job:
python_score = 85
math_score = 78
has_degree = True

if python_score >= 80 and math_score >= 70 and has_degree == True:
    print("Eligible for Data Science role")
else:
    print("Not eligible yet — keep building skills")
✅ Output
Eligible for Data Science role
🟤 Subtopic 7 — Nested if Statements

📌 You can put an if statement inside another if statement. This is called nesting.

age = 20
has_id = True

if age >= 18:
    if has_id == True:
        print("Entry allowed")
    else:
        print("Need ID to enter")
else:
    print("Too young to enter")
✅ Output
Entry allowed

⚠️ Use nesting carefully — too many levels of nesting makes code hard to read.

In Data Science, more than 2 levels of nesting is usually a sign you need to restructure your code.

❌ Common Beginner Mistakes
🚨 Mistake 1: Using = instead of == in conditions
if age = 18:    # WRONG — this is assignment not comparison
if age == 18:   # CORRECT
🚨 Mistake 2: Forgetting the colon after if/elif/else
if marks >= 50    # WRONG — missing colon
if marks >= 50:   # CORRECT
🚨 Mistake 3: Wrong indentation
if marks >= 50:
print("Passed")    # WRONG — not indented
if marks >= 50:
    print("Passed")  # CORRECT — indented 4 spaces
🚨 Mistake 4: Condition order in elif
# WRONG order
if marks >= 50:
    print("D")
elif marks >= 90:
    print("A")
# CORRECT order
if marks >= 90:
    print("A")
elif marks >= 50:
    print("D")
🎤 Interview Questions & Answers
❓Q1: What is the difference between if/else and if/elif/else?

✅ if/else handles two outcomes — True or False.

✅ if/elif/else handles multiple outcomes — you can check as many conditions as needed using elif.

❓Q2: What happens if multiple elif conditions are True?

✅ Python checks from top to bottom and executes only the FIRST condition that is True.

All remaining conditions are skipped even if they are also True.

❓Q3: Is else mandatory in Python?

✅ No. else is optional.

You can have just an if, or if with elif, without an else block.

❓Q4: What is the difference between and and or?

✅ and requires ALL conditions to be True.

✅ or requires at least ONE condition to be True.

❓Q5: Where is if/elif/else used in real Data Science?

✅ Data validation

✅ Feature engineering

✅ Model selection

✅ Threshold-based classification

✅ Handling missing values

✅ Business rule encoding in pipelines