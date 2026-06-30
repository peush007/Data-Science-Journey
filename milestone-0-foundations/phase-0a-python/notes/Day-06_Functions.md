# Day 06 — Functions

## What is a Function?

A function is a named, reusable block of code that performs a specific task. Instead of writing the same logic again and again, you write it once inside a function and call it whenever you need it.

Think of it like this:

* A function is a machine. You give it raw materials (inputs), it processes them, and gives you a finished product (output). You build the machine once. After that you just feed it inputs whenever you need that same processing done.
* Without functions — you copy paste the same calculation logic every time you need it, anywhere in your code.
* With functions — you write the logic once, give it a name, and call that name whenever you need it. Python does the rest automatically.

Python functions are one of the most used building blocks that every Data Scientist relies on daily.

---

## Why Functions Matter in Data Science

In Data Science you repeat the same operations constantly. Clean a dataset column the same way across 50 different columns. Calculate the same evaluation metric for 10 different models. Apply the same preprocessing steps to training data and test data separately.

Examples:

* Without functions you write the same cleaning logic 50 times for 50 columns
* With functions you write the cleaning logic once and call it 50 times
* Functions make code reusable, testable, and much easier to debug
* Every professional Data Science pipeline is built entirely out of functions

Without functions you cannot build a real Machine Learning pipeline. Scikit-Learn's fit(), predict(), transform() are all functions. Every model you train calls dozens of functions internally.

---

## The 2 Core Function Components

| Component     | Meaning                          | Example          |
| ------------- | --------------------------------- | ----------------- |
| Parameters    | Inputs the function accepts       | def add(a, b):    |
| Return Value  | Output the function gives back    | return a + b      |

---

## Defining and Calling a Function

A function must be defined before it can be called.

Basic Syntax:

```python
def function_name():
    # code to execute
```

Read it like this: "Define a function named function_name. When called, run this code."

---

## Without vs With a Function

Without a function — repeating logic:

```python
marks1 = 85
if marks1 >= 50:
    print("Passed")
else:
    print("Failed")

marks2 = 35
if marks2 >= 50:
    print("Passed")
else:
    print("Failed")
```

Output:

```text
Passed
Failed
```

With a function — write once, call twice:

```python
def check_result(marks):
    if marks >= 50:
        print("Passed")
    else:
        print("Failed")

check_result(85)
check_result(35)
```

Output:

```text
Passed
Failed
```

Exact same result. The function only needs to be written once. Cleaner. Reusable. Easier to fix if logic changes — only change it in one place.

---

## Real Data Science Use of Basic Functions

Example:

```python
def clean_column_name(name):
    return name.strip().lower().replace(" ", "_")

print(clean_column_name(" Customer Name "))
print(clean_column_name("ANNUAL INCOME"))
```

Output:

```text
customer_name
annual_income
```

This is one of the most common data cleaning operations in Data Science. Raw datasets often have column names with spaces, inconsistent casing, and extra whitespace. This one function fixes any column name passed to it.

---

## Parameters and Arguments

Parameters are the variable names listed in the function definition. Arguments are the actual values you pass when calling the function.

Syntax with Multiple Parameters:

```python
def function_name(param1, param2):
    # code using param1 and param2
```

---

## Functions with Multiple Parameters

Example — calculating model accuracy:

```python
def calculate_accuracy(correct_predictions, total_predictions):
    accuracy = correct_predictions / total_predictions
    return accuracy

result = calculate_accuracy(92, 100)
print(result)
```

Output:

```text
0.92
```

This is real Data Science. Every classification model's accuracy is calculated using this exact formula — correct predictions divided by total predictions.

---

## The return Statement

return sends a value back from the function to wherever it was called. Without return, a function performs actions but gives nothing back.

Syntax:

```python
def function_name():
    return value
```

Example — function with and without return:

```python
def add_no_return(a, b):
    a + b

def add_with_return(a, b):
    return a + b

result1 = add_no_return(5, 3)
result2 = add_with_return(5, 3)

print(result1)
print(result2)
```

Output:

```text
None
8
```

add_no_return calculates the sum but never sends it back, so the variable stores None. add_with_return sends the value back using return, so the variable stores the actual result.

---

## Default Parameters

You can give a parameter a default value. If the caller does not provide a value for that parameter, Python uses the default automatically.

Syntax:

```python
def function_name(param=default_value):
    # code
```

Example — train test split ratio:

```python
def split_ratio(total_samples, train_percent=80):
    train_size = int(total_samples * (train_percent / 100))
    test_size = total_samples - train_size
    return train_size, test_size

print(split_ratio(1000))
print(split_ratio(1000, train_percent=70))
```

Output:

```text
(800, 200)
(700, 300)
```

This is exactly how train_test_split() in Scikit-Learn works internally — it has a default split ratio, but you can override it whenever needed.

---

## *args — Accepting Any Number of Arguments

*args lets a function accept any number of positional arguments. Useful when you do not know in advance how many values will be passed.

Syntax:

```python
def function_name(*args):
    # args is a tuple of all values passed
```

Example — calculating average of any number of scores:

```python
def average_score(*scores):
    return sum(scores) / len(scores)

print(average_score(85, 92, 78))
print(average_score(70, 65, 90, 88, 95))
```

Output:

```text
85.0
81.6
```

The same function works whether you pass 3 scores or 5 scores. This flexibility is essential when building reusable Data Science utility functions.

---

## **kwargs — Accepting Any Number of Keyword Arguments

**kwargs lets a function accept any number of named keyword arguments. Useful when passing configuration options.

Syntax:

```python
def function_name(**kwargs):
    # kwargs is a dictionary of all key-value pairs passed
```

Example — configuring a model:

```python
def configure_model(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

configure_model(n_estimators=100, max_depth=5, random_state=42)
```

Output:

```text
n_estimators : 100
max_depth : 5
random_state : 42
```

This is exactly how Scikit-Learn models accept configuration. RandomForestClassifier(n_estimators=100, max_depth=5) uses **kwargs style logic internally to accept any combination of settings.

---

## Scope — Local vs Global Variables

Scope determines where a variable can be accessed. A variable created inside a function is local — it only exists inside that function. A variable created outside any function is global — it can be accessed anywhere.

Example:

```python
global_score = 100

def show_score():
    local_score = 50
    print("Inside function, global:", global_score)
    print("Inside function, local:", local_score)

show_score()
print("Outside function, global:", global_score)
```

Output:

```text
Inside function, global: 100
Inside function, local: 50
Outside function, global: 100
```

Trying to print local_score outside the function would cause an error, because local_score does not exist outside the function where it was created.

---

## Functions Calling Functions — Building a Pipeline

Real Data Science pipelines are built by chaining multiple small functions together.

Example:

```python
def remove_missing(data):
    return [x for x in data if x is not None]

def calculate_average(data):
    return sum(data) / len(data)

def process_pipeline(raw_data):
    clean_data = remove_missing(raw_data)
    average = calculate_average(clean_data)
    return average

raw_scores = [85, None, 92, None, 78, 90]
final_result = process_pipeline(raw_scores)
print(final_result)
```

Output:

```text
86.25
```

This is exactly how production Data Science pipelines work — small functions, each doing one job, chained together to process raw data into a final result.

---

## When to Use What

| Situation                                          | Use                  |
| --------------------------------------------------- | --------------------- |
| Fixed number of inputs known                         | Regular parameters    |
| Some inputs are optional with a sensible default     | Default parameters    |
| Unknown number of values to pass                     | *args                 |
| Unknown number of named settings to pass             | **kwargs              |
| Need to send a result back                           | return                |
| Need to repeat the same logic across the codebase    | Function               |

---

## Real Data Science Applications

| Application                              | Function Concept Used                          |
| ----------------------------------------- | ----------------------------------------------- |
| Clean column names across dataset         | Basic function with one parameter               |
| Calculate accuracy, precision, recall     | Function with multiple parameters and return     |
| Train test split with custom ratio        | Default parameters                              |
| Average of any number of metrics          | *args                                            |
| Configure ML model settings               | **kwargs                                         |
| Build multi step preprocessing pipeline   | Functions calling functions                      |

---

## Interview Questions

Q: What is a function in Python?

A: A function is a named, reusable block of code that performs a specific task and can be called multiple times without rewriting the logic.

Q: What is the difference between a parameter and an argument?

A: A parameter is the variable name listed in the function definition. An argument is the actual value passed to the function when it is called.

Q: What does the return statement do?

A: It sends a value back from the function to the place where the function was called. Without return, the function gives back None.

Q: What is the difference between *args and **kwargs?

A: *args collects any number of positional arguments into a tuple. **kwargs collects any number of keyword arguments into a dictionary.

Q: What is the difference between local and global scope?

A: A local variable exists only inside the function where it was created. A global variable exists outside all functions and can be accessed from anywhere in the code.

Q: Why are functions important in Data Science?

A: They allow the same data cleaning, transformation, and evaluation logic to be reused across multiple columns, datasets, and models without duplicating code, making pipelines reliable and easy to maintain.

---

## Key Takeaway

Functions are the building blocks of every Data Science pipeline.

Every cleaning step, every metric calculation, every model configuration is wrapped inside a function. A Data Scientist who writes clean, reusable functions can build pipelines that scale from one dataset to a thousand datasets without rewriting a single line of core logic.