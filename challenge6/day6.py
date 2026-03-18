n = int(input("Enter number of transactions: "))
transactions = []
for i in range(n):
    t = int(input("Enter transaction amount: "))
    transactions.append(t)
transaction_data = {
    "invalid": [t for t in transactions if t <= 0],
    "normal": [t for t in transactions if 1 <= t <= 500],
    "large": [t for t in transactions if 501 <= t <= 2000],
    "high_risk": [t for t in transactions if t > 2000]
}
valid_txn = [t for t in transactions if t > 0]
total_value = sum(valid_txn)
count = len(transactions)
summary = (total_value, count)
frequent = count > 5
large_spending = total_value > 5000
suspicious = len(transaction_data["high_risk"]) >= 3
if suspicious:
    risk = "High Risk"
elif large_spending or frequent:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"
print("Categorized Transactions:", transaction_data)
print("Total Transaction Value:", summary[0])
print("Number of Transactions:", summary[1])
print("Risk Classification:", risk)