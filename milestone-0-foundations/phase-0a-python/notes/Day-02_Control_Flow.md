Topic: Control Flow — if / elif / else
📖 What is Control Flow?

Control Flow is the mechanism that determines the order in which statements are executed in a program.

By default, Python executes instructions from top to bottom, one line at a time. However, real-world applications rarely follow a straight path. Programs often need to make decisions based on data, user input, or conditions. Control Flow provides this decision-making capability.

In simple words, Control Flow allows a program to choose different execution paths depending on whether a condition is True or False.

Without Control Flow, every program would execute exactly the same way every time, regardless of the data it receives.

🌍 Real World Analogy

Imagine you are standing at a traffic signal.

If the light is Green → Move.
If the light is Yellow → Slow down.
Else (Red) → Stop.

Your action depends on a condition.

Computers work in exactly the same way. They evaluate conditions and then decide what action to perform.

🤖 Why Control Flow Matters in Data Science

Every intelligent system makes decisions.

Examples:

Netflix Recommendations

If a user watches thriller movies frequently:

Recommend thriller movies.

Else:

Recommend another category.
Fraud Detection

If transaction amount > ₹1,00,000:

Flag transaction for review.

Else:

Process normally.
Customer Segmentation

If purchase amount ≥ ₹10,000:

Platinum Customer

Else if purchase amount ≥ ₹5,000:

Gold Customer

Else:

Basic Customer

Every Machine Learning system ultimately makes decisions based on conditions and rules.

🔹 The if Statement

The if statement is the simplest decision-making structure in Python.

It checks a condition.

If the condition evaluates to True, the block of code inside the if statement executes.

If the condition evaluates to False, Python skips the block.

Syntax
if condition:
    statement
Example
marks = 85

if marks >= 50:
    print("You passed!")
Output
You passed!
Explanation

Python evaluates:

85 >= 50

Result:

True

Since the condition is True, Python executes the print statement.

🔹 The if / else Statement

The if statement only handles one outcome.

But many situations require two possible outcomes.

This is where else is used.

Syntax
if condition:
    statement
else:
    statement
Example
marks = 35

if marks >= 50:
    print("You passed!")
else:
    print("You failed!")
Output
You failed!
Explanation

Python evaluates:

35 >= 50

Result:

False

Since the condition is False, the else block executes.

🔹 The if / elif / else Statement

Many real-world situations have more than two possible outcomes.

For these situations Python provides elif (Else If).

Python checks conditions from top to bottom.

The first condition that becomes True is executed.

After that, all remaining conditions are skipped.

Syntax
if condition1:
    statement

elif condition2:
    statement

elif condition3:
    statement

else:
    statement
Example
marks = 72

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Failed")
Output
Grade C
Dry Run

90 condition → False

75 condition → False

60 condition → True

Execute Grade C

Stop checking remaining conditions

🔹 Comparison Operators

Comparison operators compare two values and return either True or False.

Operator	Meaning
==	Equal To
!=	Not Equal To
>	Greater Than
<	Less Than
>=	Greater Than or Equal To
<=	Less Than or Equal To
Example
age = 18

if age == 18:
    print("Exactly 18")
🔹 Logical Operators

Logical operators combine multiple conditions.

AND Operator

All conditions must be True.

if age >= 18 and has_id:
OR Operator

At least one condition must be True.

if is_student or is_teacher:
NOT Operator

Reverses the condition.

if not is_banned:
🔹 Nested if Statements

An if statement inside another if statement is called Nested if.

Example
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
Output
Entry Allowed
Explanation

Step 1:
Check age condition.

Step 2:
If age condition passes, check ID condition.

Step 3:
Allow entry only when both conditions are satisfied.

⚠️ Common Beginner Mistakes
Mistake 1

Using = instead of ==

Wrong:

if age = 18:

Correct:

if age == 18:
Mistake 2

Missing colon

Wrong:

if marks >= 50

Correct:

if marks >= 50:
Mistake 3

Wrong indentation

Wrong:

if marks >= 50:
print("Passed")

Correct:

if marks >= 50:
    print("Passed")
🎯 Interview Questions
Q1. What is Control Flow?

Control Flow determines the order in which program statements execute based on conditions and decisions.

Q2. Difference between if and if/else?

if handles one outcome.

if/else handles two outcomes.

Q3. Difference between if/elif/else and multiple if statements?

if/elif/else executes only the first matching condition.

Multiple if statements evaluate every condition independently.

Q4. Is else mandatory?

No.

else is optional.

Q5. What happens if multiple elif conditions are True?

Only the first True condition executes.