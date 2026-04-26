# 🎓 Academic Data Drift & Copy Behavior Analyzer

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=6C63FF&height=200&section=header&text=Data%20Drift%20Analyzer&fontSize=35&fontColor=ffffff&animation=fadeIn" />
</p>

---

## 🚀 Overview
This project simulates student academic data using nested data structures and analyzes how **shallow copy vs deep copy** impacts data integrity. It applies controlled mutations and detects **data drift** using statistical methods.

---

## ⚙️ Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Math](https://img.shields.io/badge/Math_Module-FF6F00?style=for-the-badge)
![Random](https://img.shields.io/badge/Random_Module-4CAF50?style=for-the-badge)
![Copy](https://img.shields.io/badge/Copy_Module-9C27B0?style=for-the-badge)

---

## 🧠 Core Concepts

![Shallow Copy Issue](https://img.shields.io/badge/Concept-Shallow_Copy_Issue-critical?style=for-the-badge)
![Deep Copy Safe](https://img.shields.io/badge/Concept-Deep_Copy_Safe-success?style=for-the-badge)
![Data Integrity](https://img.shields.io/badge/Concept-Data_Integrity-important?style=for-the-badge)
![Data Drift](https://img.shields.io/badge/Concept-Data_Drift-analysis?style=for-the-badge)

---

## 🔍 Problem Statement
The system generates academic data and creates shallow and deep copies. Mutations are applied only to copied data to detect unintended changes in original data, analyze copy behavior failure, and measure data drift.

---

## ⚡ Approach
- Generate random student dataset using nested dictionaries  
- Apply roll-number-based mutation rule  
- Create shallow and deep copies  
- Apply transformations (sqrt, scaling)  
- Compute mean (manual + NumPy), standard deviation, drift  
- Detect copy failure and classify data drift  

---

## 🎯 Personalization Applied
Roll Number: **24110011640**

24110011640 % 3 = 0 → adjusted to 1  
Rule: `i % 1 == 0`

➡️ All student records are modified (marks, attendance, scores)

---

## 📊 Output Includes
- Original DataFrame  
- Shallow Copy DataFrame  
- Deep Copy DataFrame  
- Drift Value  
- Normalized Marks  
- Tuple Output: `(mean, drift, std_deviation)`  
- Final Classification  

---

## 🧪 Key Observation

| Copy Type     | Behavior |
|--------------|--------|
| Shallow Copy | ❌ Affects original (shared references) |
| Deep Copy    | ✅ Independent (safe) |

---

## ❗ Why Shallow Copy Fails
Shallow copy only duplicates the outer structure. Inner mutable objects remain shared, so modifying copied data also changes the original.

---

## ✅ Why Deep Copy Works
Deep copy creates completely independent objects. Changes in copied data do not affect the original dataset.

---

## 📈 Classification Logic

Drift < Threshold → Stable Data  
Drift < 2 × Threshold → Minor Drift  
Drift ≥ 2 × Threshold → Critical Drift  
Original Modified → Copy Failure Detected  

---

## 💡 Key Learning
- Difference between shallow and deep copy  
- Handling nested data structures  
- Detecting data drift using statistics  
- Understanding mutation impact  
- Writing structured Python programs  

---

## 📁 Project Structure

project/  
│── main.py  
│── utils.py  
│── README.md  

---

## 🏁 Final Insight
Shallow copy can cause unintended data modification, while deep copy ensures complete data safety. Data drift analysis helps identify hidden inconsistencies and improves data reliability.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=6C63FF&height=120&section=footer"/>
</p>
