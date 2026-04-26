# 🧠 Smart Inventory Mutation Tracker

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=4A00E0,8E2DE2&height=200&section=header&text=Inventory%20Mutation%20Analysis&fontSize=35&fontColor=ffffff&animation=fadeIn" />
</p>

---

## 📖 Problem Statement
A warehouse system maintains inventory using nested dictionaries.  
This project analyzes how data behaves when copied using:

- Shallow Copy  
- Deep Copy  

Mutations are applied and the system checks whether the original data is affected.

---

## ⚙️ Requirements Covered

✔ Functions used (create_inventory, apply_discount, compare_data)  
✔ Shallow copy & Deep copy  
✔ Roll-number-based mutation  
✔ Nested dictionary handling  
✔ Comparison logic  
✔ Output summary  

---

## 🎯 Personalization Applied

Roll Number: 24110011640  

Length = 2  
24110011640 % 2 = 0  

➡️ Modify only index 0 (Laptop)  

---

## 🧠 Logic Explanation

Shallow copy creates a new outer structure but shares inner dictionaries.  
So changes affect original.

Deep copy creates a completely independent structure.  
So changes do NOT affect original.

---

## 🔍 Output (Expected)

Original Inventory:
Laptop → changed (45000, 7, rating 4.0) ❌  
Phone → unchanged  

Shallow Copy:
Same as original → proves shared data  

Deep Copy:
Laptop changed  
Original remains same → proves independence  

---

## 📊 Differences Observed

🔴 Shallow Copy  
Original also changed ❌  
Reason: inner dictionary shared  

🟢 Deep Copy  
Original not affected ✅  
Reason: fully independent copy  

---

## 📈 Tuple Summary

Shallow → (1, 1)  
Deep → (1, 1)  

---

## 💡 Final Insight

Shallow copy causes data corruption in nested structures.  
Deep copy ensures safe and independent data handling.

---

## 🎯 Conclusion

This project shows why deep copy is essential in real-world systems where data integrity matters.

---

## 🚀 How to Run

```bash
python inventory_tracker.py
```
