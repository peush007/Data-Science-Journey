# ===================================================
# Day 06 — Functions
# Milestone 0 | Phase 0A | Python Mastery
# ===================================================


# ===================================================
# Lab 1 — Basic Function (No Parameters)
# ===================================================
def greet():
    print("Hello, welcome to Day 6!")

greet()

# Expected Output:
# Hello, welcome to Day 6!


# ===================================================
# Lab 2 — Function with One Parameter
# ===================================================
def check_result(marks):
    if marks >= 50:
        print("Passed")
    else:
        print("Failed")

check_result(85)
check_result(35)

# Expected Output:
# Passed
# Failed


# ===================================================
# Lab 3 — Real DS Use: Clean Column Name Function
# ===================================================
def clean_column_name(name):
    return name.strip().lower().replace(" ", "_")

print(clean_column_name(" Customer Name "))
print(clean_column_name("ANNUAL INCOME"))

# Expected Output:
# customer_name
# annual_income


# ===================================================
# Lab 4 — Function with Multiple Parameters
# ===================================================
def calculate_accuracy(correct_predictions, total_predictions):
    accuracy = correct_predictions / total_predictions
    return accuracy

result = calculate_accuracy(92, 100)
print(result)

# Expected Output:
# 0.92


# ===================================================
# Lab 5 — Function With and Without Return
# ===================================================
def add_no_return(a, b):
    a + b

def add_with_return(a, b):
    return a + b

result1 = add_no_return(5, 3)
result2 = add_with_return(5, 3)

print(result1)
print(result2)

# Expected Output:
# None
# 8


# ===================================================
# Lab 6 — Default Parameters: Train Test Split Ratio
# ===================================================
def split_ratio(total_samples, train_percent=80):
    train_size = int(total_samples * (train_percent / 100))
    test_size = total_samples - train_size
    return train_size, test_size

print(split_ratio(1000))
print(split_ratio(1000, train_percent=70))

# Expected Output:
# (800, 200)
# (700, 300)


# ===================================================
# Lab 7 — *args: Average of Any Number of Scores
# ===================================================
def average_score(*scores):
    return sum(scores) / len(scores)

print(average_score(85, 92, 78))
print(average_score(70, 65, 90, 88, 95))

# Expected Output:
# 85.0
# 81.6


# ===================================================
# Lab 8 — **kwargs: Configuring a Model
# ===================================================
def configure_model(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

configure_model(n_estimators=100, max_depth=5, random_state=42)

# Expected Output:
# n_estimators : 100
# max_depth : 5
# random_state : 42


# ===================================================
# Lab 9 — Local vs Global Scope
# ===================================================
global_score = 100

def show_score():
    local_score = 50
    print("Inside function, global:", global_score)
    print("Inside function, local:", local_score)

show_score()
print("Outside function, global:", global_score)

# Expected Output:
# Inside function, global: 100
# Inside function, local: 50
# Outside function, global: 100


# ===================================================
# Lab 10 — Functions Calling Functions (Mini Pipeline)
# ===================================================
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

# Expected Output:
# 86.25