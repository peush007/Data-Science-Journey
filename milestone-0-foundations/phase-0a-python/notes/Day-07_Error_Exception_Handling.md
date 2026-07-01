# Day 07 — Error & Exception Handling

## What is an Error?

An error is Python's way of telling you that something went wrong during the execution of your program. When Python encounters something it cannot handle, it stops running and displays an error message called a traceback.

Think of it like this:

* A car has a dashboard with warning lights. When something goes wrong — low fuel, engine problem, tyre pressure — a specific warning light turns on telling you exactly what the problem is.
* Python errors work the same way. Each error has a specific name and message that tells you exactly what went wrong and where.
* Without understanding errors you cannot debug your code.
* Without exception handling you cannot build programs that survive unexpected situations.

In Data Science, unexpected situations happen constantly — missing files, corrupted data, network failures, wrong data types. A program that crashes every time something unexpected happens is useless in production.

---

## Why Error Handling Matters in Data Science

In Data Science your programs work with real world data. Real world data is messy, unpredictable, and full of surprises.

Examples:

* A CSV file your program expects does not exist on the server
* A dataset column contains a string where your code expects a number
* A user passes an empty dataset to your model training function
* An API you are fetching data from times out unexpectedly
* A dataset column contains None where your calculation expects a value

Without exception handling all of these situations crash your program completely. With exception handling your program catches the problem, handles it gracefully, logs what went wrong, and either continues or shuts down cleanly with a meaningful message.

Every production Data Science pipeline has exception handling built into every stage. Without it, one bad row in a million row dataset would crash the entire pipeline and lose all processed results.

---

## The 3 Core Error Handling Components

| Component | Purpose                                | Syntax          |
| --------- | -------------------------------------- | --------------- |
| try       | Code that might cause an error         | try:            |
| except    | What to do if error occurs             | except ErrorType: |
| finally   | Code that always runs no matter what   | finally:        |

---

## Types of Common Python Errors

Before handling errors you need to know what errors exist.

| Error Type           | When It Happens                              | Example                  |
| -------------------- | -------------------------------------------- | ------------------------ |
| ValueError           | Wrong value type passed                      | int("hello")             |
| TypeError            | Wrong data type used                         | "5" + 5                  |
| ZeroDivisionError    | Dividing by zero                             | 10 / 0                   |
| FileNotFoundError    | File does not exist                          | open("missing.csv")      |
| IndexError           | Accessing index that does not exist          | list[10] on 5-item list  |
| KeyError             | Accessing dictionary key that does not exist | dict["missing_key"]      |
| AttributeError       | Calling method that does not exist           | None.lower()             |
| NameError            | Using variable that was never defined        | print(undefined_var)     |

---

## Without vs With Exception Handling

Without exception handling — program crashes:

```python
numbers = [10, 20, 0, 30]

for num in numbers:
    result = 100 / num
    print(result)
```

Output:

```text
10.0
5.0
ZeroDivisionError: division by zero
```

Program crashed at 0. The value 30 was never processed. All remaining work is lost.

With exception handling — program survives:

```python
numbers = [10, 20, 0, 30]

for num in numbers:
    try:
        result = 100 / num
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero — skipping this value")
```

Output:

```text
10.0
5.0
Cannot divide by zero — skipping this value
3.3333333333333335
```

Program caught the error, handled it gracefully, and continued processing the remaining values. In a real dataset with millions of rows, this difference is the difference between a pipeline that works and one that is useless.

---

## The try / except Block

Basic Syntax:

```python
try:
    # code that might cause an error
except ErrorType:
    # code that runs if that specific error occurs
```

Read it like this: "Try to run this code. If this specific error occurs, run this instead."

---

## Handling Multiple Errors

You can handle different errors differently in the same block.

Syntax:

```python
try:
    # code
except ErrorType1:
    # handle first type of error
except ErrorType2:
    # handle second type of error
```

Real Data Science Example — loading and processing a dataset column:

```python
def process_value(value):
    try:
        result = 100 / int(value)
        return result
    except ZeroDivisionError:
        print("Value is zero — returning 0")
        return 0
    except ValueError:
        print("Value cannot be converted to integer:", value)
        return None

print(process_value(25))
print(process_value(0))
print(process_value("abc"))
```

Output:

```text
4.0
Value is zero — returning 0
0
Value cannot be converted to integer: abc
None
```

This is exactly how production Data Science pipelines handle bad data — catch each possible error separately, handle each one appropriately, and return a safe default value instead of crashing.

---

## The else Block

The else block runs only if NO error occurred in the try block.

Syntax:

```python
try:
    # code that might fail
except ErrorType:
    # runs if error occurs
else:
    # runs only if NO error occurred
```

Example:

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Division successful:", result)
        return result

safe_divide(10, 2)
safe_divide(10, 0)
```

Output:

```text
Division successful: 5.0
Cannot divide by zero
```

---

## The finally Block

The finally block always runs — whether an error occurred or not. It is used for cleanup operations that must happen no matter what.

Syntax:

```python
try:
    # code that might fail
except ErrorType:
    # runs if error occurs
finally:
    # always runs no matter what
```

Real Data Science Example — closing a file after reading:

```python
def read_dataset(filename):
    try:
        file = open(filename, "r")
        data = file.read()
        print("File loaded successfully")
        return data
    except FileNotFoundError:
        print("Error: File not found —", filename)
        return None
    finally:
        print("Cleanup complete — closing resources")

read_dataset("sales_data.csv")
read_dataset("missing_file.csv")
```

Output:

```text
Error: File not found — sales_data.csv
Cleanup complete — closing resources
Error: File not found — missing_file.csv
Cleanup complete — closing resources
```

The finally block is critical in Data Science pipelines where you open database connections, file handles, or API sessions. Even if something crashes, you must close those connections to avoid memory leaks and resource exhaustion.

---

## Raising Custom Errors — raise

You can raise your own errors intentionally when your code receives invalid input.

Syntax:

```python
raise ErrorType("Your custom message here")
```

Real Data Science Example — validating dataset before training:

```python
def validate_dataset(data):
    if len(data) == 0:
        raise ValueError("Dataset is empty. Cannot train model on empty data.")
    if len(data) < 100:
        raise ValueError("Dataset too small. Minimum 100 samples required.")
    print("Dataset valid. Samples:", len(data))

try:
    validate_dataset([])
except ValueError as e:
    print("Validation Error:", e)

try:
    validate_dataset([1, 2, 3])
except ValueError as e:
    print("Validation Error:", e)

try:
    validate_dataset(list(range(500)))
except ValueError as e:
    print("Validation Error:", e)
```

Output:

```text
Validation Error: Dataset is empty. Cannot train model on empty data.
Validation Error: Dataset too small. Minimum 100 samples required.
Dataset valid. Samples: 500
```

This is exactly how professional ML pipelines validate data before training begins. Instead of letting a model silently train on empty or tiny datasets and produce meaningless results, you catch the problem immediately with a clear, meaningful error message.

---

## Catching Any Error — Generic except

Sometimes you want to catch any error regardless of its type.

```python
try:
    # risky code
except Exception as e:
    print("An unexpected error occurred:", e)
```

The as e part stores the actual error message in variable e so you can print or log it.

Real Data Science Example — safe data pipeline step:

```python
def safe_pipeline_step(data, step_name):
    try:
        result = [x * 2 for x in data]
        print(step_name, "completed successfully")
        return result
    except Exception as e:
        print(step_name, "failed:", e)
        return None

output = safe_pipeline_step([1, 2, 3], "Feature Scaling")
print(output)

output2 = safe_pipeline_step("not a list of numbers", "Feature Scaling")
print(output2)
```

Output:

```text
Feature Scaling completed successfully
[2, 4, 6]
Feature Scaling failed: can't multiply sequence by non-int of type 'str'
None
```

---

## Complete Exception Handling Structure

```python
try:
    # Code that might fail
except SpecificError:
    # Handle specific error
except AnotherError:
    # Handle another specific error
except Exception as e:
    # Handle any other unexpected error
else:
    # Runs only if no error occurred
finally:
    # Always runs — cleanup code
```

---

## When to Use What

| Situation                                        | Use                           |
| ------------------------------------------------- | ----------------------------- |
| Code might fail in a predictable way              | try / except with specific error type |
| Need to handle multiple error types differently   | Multiple except blocks        |
| Need to run code only on success                  | else block                    |
| Must close files, connections, resources          | finally block                 |
| Want to enforce rules on incoming data            | raise with custom message     |
| Unknown error type, want to log everything        | except Exception as e         |

---

## Real Data Science Applications

| Application                               | Exception Handling Used         |
| ------------------------------------------ | -------------------------------- |
| Loading CSV files from disk                | FileNotFoundError                |
| Converting string columns to numbers       | ValueError                       |
| Dividing values (calculating ratios)       | ZeroDivisionError                |
| Accessing dataset columns by name          | KeyError                         |
| Validating dataset size before training    | raise ValueError                 |
| Closing database connections after query   | finally block                    |
| Logging pipeline step failures             | except Exception as e            |

---

## Interview Questions

Q: What is exception handling in Python?

A: Exception handling is a mechanism that allows a program to catch errors that occur during execution, handle them gracefully, and continue running instead of crashing completely.

Q: What is the difference between try/except and try/except/finally?

A: try/except catches errors and handles them. finally adds a block that always executes regardless of whether an error occurred or not — used for cleanup like closing files or database connections.

Q: What is the difference between except ErrorType and except Exception as e?

A: except ErrorType catches one specific type of error only. except Exception as e catches any error of any type and stores the error message in variable e so it can be logged or displayed.

Q: When should you use raise?

A: When your function receives invalid input that would cause incorrect results downstream. Instead of silently processing bad data, you raise an error immediately with a clear message explaining exactly what is wrong.

Q: What does the else block do in exception handling?

A: The else block runs only if the try block completed without any error. It separates the success path logic from the error handling logic.

Q: Why is exception handling critical in Data Science pipelines?

A: Real world data is unpredictable. Missing files, wrong data types, empty datasets, division by zero — all happen constantly. Without exception handling one bad row crashes the entire pipeline and loses all processed results.

---

## Key Takeaway

Exception handling is what separates a script that works on clean data from a pipeline that works in production.

Real world Data Science data is messy, incomplete, and full of surprises. Every professional pipeline wraps every risky operation in try/except, validates every input with raise, and cleans up every resource in finally. A Data Scientist who writes proper exception handling builds systems that are reliable, debuggable, and production-ready.