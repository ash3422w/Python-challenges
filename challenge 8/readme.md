
# Multi-Dimensional Academic Intelligence System

## 📌 Project Overview
This project analyzes student performance using multiple dimensions such as **marks, attendance, and assignment scores**.  
It uses Python along with **NumPy and Pandas** to perform statistical analysis and classification.

---

## 🎯 Objectives
- Generate student data using random values
- Store data using Python data structures
- Perform multi-layer analysis
- Classify students based on performance
- Provide final academic insights

---

## 🛠️ Technologies Used
- Python
- NumPy
- Pandas
- math module
- random module

---

## 📊 Data Structure
Each student record contains:
- student_id
- marks (0–100)
- attendance_percentage (0–100)
- assignment_score (0–50)

All records are stored in a **list of tuples** and then converted into a **Pandas DataFrame**.

---

## ⚙️ Features

### 1. Data Generation
- Generates minimum 10 students
- Uses random values for marks, attendance, and assignment

---

### 2. Student Classification
Students are categorized as:

| Condition | Category |
|----------|--------|
| marks < 40 OR attendance < 50 | At Risk |
| marks 40–70 | Average |
| marks 71–90 | Good |
| marks > 90 AND attendance > 80 | Top Performer |
### 3. Performance Index

performance_index = (marks * 0.6 + assignment * 0.4) * log(attendance + 1)


#### Why this works:
- Gives more importance to marks
- Includes assignment performance
- Uses logarithmic scaling for attendance to avoid extreme impact
- Ensures balanced evaluation

---

### 4. Statistical Analysis
- Mean (manual calculation)
- Median
- Standard Deviation
- Correlation (marks vs attendance)
- Normalization of marks

---

### 5. Pattern Detection
- Consistency → std deviation < 15
- Attendance Risk → more than 3 students below 50%
- High Achievement → at least 2 top performers

---

## 📈 Final Output
The system displays:
- DataFrame table
- Categorized dictionary
- Statistical summary
- Tuple → (mean, std_dev, max_marks)
- Final system insight:
  - Stable Academic System
  - Moderate Performance
  - Critical Attention Required

---

## 📂 Functions Used
- `generate_data()`
- `classify_students()`
- `analyze_data()`

---

## 📌 Requirements
Install dependencies:

pip install numpy pandas


---

## 🚀 How to Run

python main.py


---

## 📎 Notes
- Uses lists, tuples, sets, and dictionaries
- Includes list comprehension
- Avoids built-in `.describe()` for manual calculation

---

## 👨‍💻 Author
Ashok Reddy

---

### 3. Performance Index
