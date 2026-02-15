D = 0
n = int(input("Enter number of activity scores: "))
scores = []
for i in range(n):
    num = int(input("Enter score: "))
    scores.append(num)
low_risk = []
medium_risk = []
high_risk = []
critical_risk = []
valid = 0
ignored = 0
for i in range(n):
    if scores[i] < 0:
        ignored = ignored + 1
    else:
        valid = valid + 1
        if scores[i] <= 30:
            low_risk.append(scores[i])
        elif scores[i] <= 60:
            medium_risk.append(scores[i])
        elif scores[i] <= 100:
            high_risk.append(scores[i])
        else:
            critical_risk.append(scores[i])
print("Register Digit (D):", D)
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)
removed = 0
print("After Personalized Filtering:")
for i in low_risk:
    removed = removed + 1
low_risk = []
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)
print("Total Valid Entries:", valid)
print("Ignored Entries:", ignored)
print("Removed Due to Personalization:", removed)
