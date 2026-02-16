full_name = "Ashok Reddy"
L = 0
for ch in full_name:
    if ch != " ":
        L = L + 1
PLI =L%3
requests = []
n = int(input("Enter number of resource requests: "))
for i in range(n):
    value = int(input("Enter the resource request :"))
    requests.append(value)
low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []
total_valid = 0
for value in requests:
    if value < 0:
        invalid_requests.append(value)
    elif value == 0:
        total_valid = total_valid + 1
    elif value >= 1 and value <= 20:
        low_demand.append(value)
        total_valid = total_valid + 1
    elif value >= 21 and value <= 50:
        moderate_demand.append(value)
        total_valid = total_valid + 1
    else:
        high_demand.append(value)
        total_valid = total_valid + 1
applied_rule = "Rule B (Remove High Demand)"
removed_count = len(high_demand)
high_demand = []
print("\nFull Name:", full_name)
print("L Value:", L)
print("PLI Value:", PLI)
print("Applied Rule:", applied_rule)
print("Total Valid Requests:", total_valid)
print("Removed Due to PLI:", removed_count)
print("Final Low Demand List:", low_demand)
print("Final Moderate Demand List:", moderate_demand)
print("Final High Demand List:", high_demand)
print("Invalid Requests:", invalid_requests)
