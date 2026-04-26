
# 🧠 Smart Inventory Mutation Tracker

---

## 📖 Problem Understanding
This project analyzes how inventory data stored as nested dictionaries behaves when copied using shallow copy and deep copy. Modifications like price and stock updates are applied only to copied data, and the program checks whether these changes affect the original data. This helps in understanding data consistency and copy behavior.

---

## ⚙️ Logic / Approach Used
- Create inventory using nested dictionaries  
- Generate shallow and deep copies  
- Apply mutation based on roll number  
- Compare original and modified data  
- Analyze which copy affects original  

---

## 🎯 Personalization Applied
- **Roll Number:** 24110011640  
- **Formula:** `roll_number % len(data)`  
- **Result:** Index `1` (Phone item modified)  

---

## 🧪 Test Case Verification
- Shallow copy → original data changed ❌  
- Deep copy → original data unchanged ✅  
- Confirms correct detection of copy behavior  

---

## 🔍 Analysis

### Which copy affected original?
➡️ Shallow Copy  

### Which remained independent?
➡️ Deep Copy  

### Why behavior differs?
Shallow copy shares nested references, so changes affect original data.  
Deep copy creates independent objects, so original remains unchanged.  

---

## 📊 Example Insight
- Modifying shallow copy → original also changes  
- Modifying deep copy → original stays same  

---

## 📘 Learning Outcome
I learned the difference between shallow and deep copy in nested data structures. I understood how shallow copy can unintentionally modify original data, while deep copy ensures safe and independent data handling. I also improved my understanding of Python functions and data comparison.

---

## 🚀 How to Run
```bash
python inventory_tracker.py
