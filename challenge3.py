n = int(input("Enter number of students: "))
marks = [0] * n
for i in range(n):
    marks[i] = int(input(f"Enter the marks{i}:"))
valid = 0
fail = 0
for j in marks:
    j = j - 2 #MY REG NO IS 640(EVEN)
    if j < 0 or j > 100:
        print(j, "→ Invalid")
    elif j >= 90:
        valid += 1
        print(j, "→ Excellent")
    elif j >= 75:
        valid += 1
        print(j, "→ Very Good")
    elif j >= 60:
        valid += 1
        print(j, "→ Good")
    elif j >= 40:
        valid += 1
        print(j, "→ Average")
    else:
        valid += 1
        fail+= 1
        print(j, "→ Fail")
print("Total Valid Students:", valid)
print("Total Failed Students:", fail)
