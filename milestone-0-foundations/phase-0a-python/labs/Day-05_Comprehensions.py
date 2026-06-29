# ================================================
# Day 05 — List & Dictionary Comprehensions
# Milestone 0 | Phase 0A | Python Mastery
# Date: 28 June 2026
# ================================================

# ── Lab 1 — Basic List Comprehension ─────────────
marks = [85, 92, 78, 65, 90]
doubled = [mark * 2 for mark in marks]
print(doubled)

# ── Lab 2 — Clean Column Names ───────────────────
columns = ["Age", "Salary", "DEPARTMENT", "City"]
clean = [col.lower() for col in columns]
print(clean)

# ── Lab 3 — Filter Passing Marks ─────────────────
marks = [85, 42, 92, 38, 78, 55, 90]
passing = [mark for mark in marks if mark >= 50]
print(passing)

# ── Lab 4 — Remove None Values ───────────────────
ages = [25, None, 30, None, 28, 35, None, 22]
clean_ages = [age for age in ages if age is not None]
print(clean_ages)

# ── Lab 5 — Create Label Column ──────────────────
marks = [85, 42, 92, 38, 78]
labels = ["Pass" if mark >= 50 else "Fail" for mark in marks]
print(labels)

# ── Lab 6 — Dictionary Comprehension ─────────────
models = ["LinearRegression", "RandomForest", "XGBoost"]
scores = [0.82, 0.91, 0.94]
results = {model: score for model, score in zip(models, scores)}
print(results)

# ── Lab 7 — Filter High Performing Models ────────
model_results = {
    "LinearRegression": 0.82,
    "RandomForest": 0.91,
    "XGBoost": 0.94,
    "SVM": 0.78
}
good_models = {m: s for m, s in model_results.items() if s >= 0.90}
print(good_models)