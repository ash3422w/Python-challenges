
# 🚨 Smart Transaction Risk Detector

## 🏫 Academic Details
- **Course**: CSE205 – Hands-on Python  
- **Challenge**: Code2Xplore – DAY-6  
- **Department**: Computer Science and Engineering  
- **University**: SRM University–AP  

---

## 📌 Problem Understanding
A digital payment system records daily transaction amounts of a user. The objective is to analyze these transactions and detect suspicious spending patterns. Each transaction is categorized into invalid, normal, large, or high-risk based on its value. After classification, pattern detection rules are applied to determine the overall risk level.

---

## 🧠 Algorithm Explanation
The program first takes transaction inputs and stores them in a list.  
Each transaction is classified into categories using list comprehension and stored in a dictionary.  
Valid transactions are filtered to calculate the total transaction value.  
A tuple is used to store summary information such as total value and number of transactions.  
Then, pattern detection rules are applied to check for frequent transactions, large spending, and suspicious activity.  
Finally, the overall risk level is determined based on these conditions.

---

## ⚙️ Features Used
- Lists  
- For loop  
- Conditional statements  
- List comprehension  
- Dictionary for classification  
- Tuple for summary  

---

## ➕ Additional Test Cases

### 🔹 Test Case 1
Input:
5
50
600
2200
0
1500

Output: Low Risk

---

### 🔹 Test Case 2
Input:
6
2500
2600
2700
100
200
300

Output: High Risk

---

## 🤔 Reflection
I decided to prioritize high-risk transactions while determining the final risk level because they indicate a stronger possibility of fraud. I also used list comprehension to simplify classification and make the code more efficient and readable.

---

## 🎯 Learning Outcome
- Learned how to use list comprehension effectively  
- Improved understanding of dictionaries and tuples  
- Applied conditional logic for pattern detection  
- Enhanced problem-solving skills in Python  
