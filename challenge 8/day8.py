import random
import math
import numpy as np
import pandas as pd
def generate_data(num_students):
    records = []
    for i in range(1, num_students + 1):
        student_id = f"S{i:03d}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        records.append((student_id, marks, attendance, assignment))
    return records
def classify_students(records):
    categories = {}
    for student_id, marks, attendance, assignment in records:
        if marks > 90 and attendance > 80:
            categories[student_id] = "Top Performer"
        elif marks < 40 or attendance < 50:
            categories[student_id] = "At Risk"
        elif 40 <= marks <= 70:
            categories[student_id] = "Average"
        elif 71 <= marks <= 90:
            categories[student_id] = "Good"
        else:
            categories[student_id] = "Average"
    return categories
def analyze_data(records):
    df = pd.DataFrame(records, columns=["student_id", "marks", "attendance_percentage", "assignment_score"])

    df["performance_index"] = [
        (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)
        for marks, attendance, assignment in zip(
            df["marks"], df["attendance_percentage"], df["assignment_score"]
        )
    ]
    categories = classify_students(records)
    df["category"] = df["student_id"].map(categories)
    marks_array = np.array(df["marks"])
    attendance_array = np.array(df["attendance_percentage"])
    mean_marks = sum(marks_array) / len(marks_array)
    sorted_marks = sorted(marks_array)
    n = len(sorted_marks)
    if n % 2 == 0:
        median_marks = (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2
    else:
        median_marks = sorted_marks[n // 2]
    variance = sum((x - mean_marks) ** 2 for x in marks_array) / len(marks_array)
    std_dev_marks = math.sqrt(variance)
    correlation = np.corrcoef(marks_array, attendance_array)[0, 1]
    min_marks = np.min(marks_array)
    max_marks = np.max(marks_array)
    if max_marks != min_marks:
        df["normalized_marks"] = [(x - min_marks) / (max_marks - min_marks) for x in df["marks"]]
    else:
        df["normalized_marks"] = [0 for _ in df["marks"]]
    consistency = std_dev_marks < 15
    attendance_risk = len([x for x in attendance_array if x < 50]) > 3
    high_achievement = len([x for x in df["category"] if x == "Top Performer"]) >= 2
    summary_tuple = (mean_marks, std_dev_marks, max_marks)
    if consistency and not attendance_risk and high_achievement:
        final_insight = "Stable Academic System"
    elif attendance_risk or std_dev_marks > 25:
        final_insight = "Critical Attention Required"
    else:
        final_insight = "Moderate Performance"
    stats = {
        "Mean Marks": mean_marks,
        "Median Marks": median_marks,
        "Standard Deviation": std_dev_marks,
        "Correlation (Marks vs Attendance)": correlation,
        "Consistency": consistency,
        "Attendance Risk": attendance_risk,
        "High Achievement": high_achievement,
        "Summary Tuple": summary_tuple,
        "Final Insight": final_insight
    }
    return df, categories, stats
def display_results(df, categories, stats, student_set):
    print("DATAFRAME TABLE")
    print(df.to_string(index=False))
    print("\nCATEGORIZED DICTIONARY")
    print(categories)
    print("\nSTUDENT ID SET")
    print(student_set)
    print("\nSTATISTICAL SUMMARY")
    for key, value in stats.items():
        print(f"{key}: {value}")
    print("\nWHY PERFORMANCE INDEX WORKS")
    print("The performance index combines marks and assignment score, giving more weight to marks.")
    print("It is then multiplied by log(attendance + 1), so better attendance increases the score")
    print("without making attendance dominate too much.")
roll_last_digit = 0
num_students = max(10, roll_last_digit)
records = generate_data(num_students)
student_set = {student_id for student_id, _, _, _ in records}
df, categories, stats = analyze_data(records)
display_results(df, categories, stats, student_set)