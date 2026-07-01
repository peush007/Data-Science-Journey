# ===================================================
# Day 07 — Error & Exception Handling
# Milestone 0 | Phase 0A | Python Mastery
# ===================================================


# ===================================================
# Lab 1 — No Exception Handling (Program Crashes)
# ===================================================
numbers = [10, 20, 0, 30]

for num in numbers:
    try:
        result = 100 / num
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero — skipping this value")

# Expected Output:
# 10.0
# 5.0
# Cannot divide by zero — skipping this value
# 3.3333333333333335


# ===================================================
# Lab 2 — Handling Multiple Errors
# ===================================================
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

# Expected Output:
# 4.0
# Value is zero — returning 0
# 0
# Value cannot be converted to integer: abc
# None


# ===================================================
# Lab 3 — try / except / else Block
# ===================================================
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

# Expected Output:
# Division successful: 5.0
# Cannot divide by zero


# ===================================================
# Lab 4 — finally Block: Always Runs
# ===================================================
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

read_dataset("missing_file.csv")

# Expected Output:
# Error: File not found — missing_file.csv
# Cleanup complete — closing resources


# ===================================================
# Lab 5 — raise: Custom Validation Errors
# ===================================================
def validate_dataset(data):
    if len(data) == 0:
        raise ValueError("Dataset is empty. Cannot train model.")
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

# Expected Output:
# Validation Error: Dataset is empty. Cannot train model.
# Validation Error: Dataset too small. Minimum 100 samples required.
# Dataset valid. Samples: 500


# ===================================================
# Lab 6 — except Exception as e: Catch Any Error
# ===================================================
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

output2 = safe_pipeline_step("not_a_list", "Feature Scaling")
print(output2)

# Expected Output:
# Feature Scaling completed successfully
# [2, 4, 6]
# Feature Scaling failed: 'str' object is not iterable
# None


# ===================================================
# Lab 7 — Complete Pipeline with Full Exception Handling
# ===================================================
def full_pipeline(raw_data, filename):
    try:
        validate_dataset(raw_data)
        clean = [x for x in raw_data if x is not None]
        average = sum(clean) / len(clean)
        print("Pipeline complete. Average:", average)
        return average
    except ValueError as e:
        print("Data Error:", e)
        return None
    except ZeroDivisionError:
        print("Error: All values were None — cannot calculate average")
        return None
    except Exception as e:
        print("Unexpected pipeline error:", e)
        return None
    finally:
        print("Pipeline finished for:", filename)

full_pipeline(list(range(200)), "dataset.csv")
full_pipeline([], "empty.csv")

# Expected Output:
# Dataset valid. Samples: 200
# Pipeline complete. Average: 99.5
# Pipeline finished for: dataset.csv
# Validation Error: Dataset is empty. Cannot train model.
# Pipeline finished for: empty.csv