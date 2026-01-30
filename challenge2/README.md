## Challenge Understanding / Description

In this challenge, a Python program is designed to validate student registration details by applying specific conditions to each input. The program will accept four inputs from the user: Student ID, Email ID, Password, and Referral Code. Each input has specific validation rules.  

If all the rules are satisfied, the account is considered **APPROVED**. If any one rule fails, the account is considered **REJECTED**.  

The validation is performed using simple conditional statements and string operations such as `len()`, `count()`, indexing, and `isdigit()`. A flag variable is used to track whether all validations pass.  

---

## Validation Rules

**Student ID:**  
- Must start with CSE  
- 4th character must be -  
- Last 3 characters must be digits  
- Example valid: CSE-245  

**Email ID:**  
- Must contain @ and .  
- @ cannot be the first or last character  
- Must end with .edu  
- Example valid: student@univ.edu  

**Password:**  
- Length ≥ 8  
- First character must be uppercase  
- Must contain at least one digit  
- Example valid: Aman1234  

**Referral Code:**  
- Must start with REF  
- Next 2 characters must be digits  
- Last character must be @  
- Example valid: REF45@  

---

## Algorithm / Steps

1. Take inputs from the user: Student ID, Email ID, Password, Referral Code.  
2. Initialize a flag variable (e.g., status = False) to track overall validation.  
3. Validate Student ID:  
   - Check length = 7  
   - Check first three characters = CSE  
   - Check 4th character = -  
   - Check last three characters are digits  
4. Validate Email ID:  
   - Must contain @ and .  
   - @ cannot be first or last character  
   - Must end with .edu  
5. Validate Password:  
   - Length ≥ 8  
   - First character must be uppercase  
   - Must contain at least one digit  
6. Validate Referral Code:  
   - Length = 6  
   - Must start with REF  
   - Next two characters must be digits  
   - Last character must be @  
7. If all validations pass, set status = True.  
8. Check the flag:  
   - If status = True → print APPROVED  
   - Else → print REJECTED  

---

## Python Program

```python
# Smart Registration System – Credential Validator
# Written by Ashok Reddy
