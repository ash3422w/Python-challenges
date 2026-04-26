import random
import math
import numpy as np
import pandas as pd
import copy

def generate_data(n=12):
    data = []
    for i in range(n):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data

def mutate_data(data, roll_number):
    mod_value = (roll_number % 3) + 1
    for i in range(len(data)):
        if i % mod_value == 0:
            data[i]["marks"] = int(data[i]["marks"] + math.sqrt(data[i]["marks"]))
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 3

def to_dataframe(data):
    return pd.DataFrame(data)

def analyze_data(original, modified):
    orig_marks = np.array([x["marks"] for x in original])
    mod_marks = np.array([x["marks"] for x in modified])

    mean_orig = np.mean(orig_marks)
    mean_mod = np.mean(mod_marks)
    std_dev = np.std(mod_marks)
    median = np.median(mod_marks)

    manual_mean = sum(orig_marks) / len(orig_marks)

    drift = abs(mean_orig - mean_mod)

    normalized = (mod_marks - np.min(mod_marks)) / (np.max(mod_marks) - np.min(mod_marks))

    return mean_mod, drift, std_dev, median, manual_mean, normalized

def classify(drift, threshold, original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    if drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"

roll_number = 24110011640

original_data = generate_data()

shallow_copy = copy.copy(original_data)
deep_copy = copy.deepcopy(original_data)

mutate_data(shallow_copy, roll_number)
mutate_data(deep_copy, roll_number)

df_original = to_dataframe(original_data)
df_shallow = to_dataframe(shallow_copy)
df_deep = to_dataframe(deep_copy)

mean, drift, std_dev, median, manual_mean, normalized = analyze_data(original_data, deep_copy)

threshold = 5

result = classify(drift, threshold, original_data, shallow_copy)

print("\n===== ORIGINAL DATA =====")
print(df_original)

print("\n===== SHALLOW COPY DATA =====")
print(df_shallow)

print("\n===== DEEP COPY DATA =====")
print(df_deep)

print("\n===== ANALYSIS =====")
print("Mean (modified):", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Manual Mean (without NumPy):", manual_mean)

print("\nDrift Value:", drift)
print("Tuple Output:", (mean, drift, std_dev))

print("\nNormalized Marks:", normalized)

print("\n===== FINAL RESULT =====")
print(result)

print("\n===== EXPLANATION =====")
print("Shallow copy caused drift because it copies only the outer list.")
print("The inner list (scores) remains shared between original and shallow copy.")
print("So when scores were modified, original data also changed unexpectedly.")
print("Deep copy avoids this by creating completely independent objects.")
