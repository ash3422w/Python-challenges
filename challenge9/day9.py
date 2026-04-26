import copy
def create_inventory():
   return [
       {"item": "Laptop", "details": {"price": 50000, "stock": 10, "rating": 4.5}},
       {"item": "Phone", "details": {"price": 20000, "stock": 25, "rating": 4.2}},
       {"item": "Tablet", "details": {"price": 30000, "stock": 15, "rating": 4.0}}
   ]
def apply_discount(data, roll_number):
   index_to_modify = roll_number % len(data)
   for i in range(len(data)):
       if i == index_to_modify:
           data[i]["details"]["price"] *= 0.9
           data[i]["details"]["stock"] += 5
def compare_data(original, modified):
   changed = 0
   unchanged = 0
   for i in range(len(original)):
       if original[i]["details"] != modified[i]["details"]:
           changed += 1
       else:
           unchanged += 1
   return changed, unchanged
def example_difference():
   original = [{"item": "Laptop", "details": {"price": 50000}}]
   shallow = copy.copy(original)
   deep = copy.deepcopy(original)
   shallow[0]["details"]["price"] = 45000
   print("\nExample After Shallow Copy Modification:")
   print("Original:", original)
   print("Shallow:", shallow)
   deep[0]["details"]["price"] = 30000
   print("\nExample After Deep Copy Modification:")
   print("Original:", original)
   print("Deep:", deep)
roll_number = 24110011640
original_inventory = create_inventory()
shallow_copy = copy.copy(original_inventory)
deep_copy = copy.deepcopy(original_inventory)
apply_discount(shallow_copy, roll_number)
apply_discount(deep_copy, roll_number)
shallow_result = compare_data(original_inventory, shallow_copy)
deep_result = compare_data(original_inventory, deep_copy)
print("\n--- Original Inventory ---")
print(original_inventory)
print("\n--- Shallow Copy ---")
print(shallow_copy)
print("\n--- Deep Copy ---")
print(deep_copy)
print("\nShallow Copy Changes (changed, unchanged):", shallow_result)
print("Deep Copy Changes (changed, unchanged):", deep_result)
print("\n--- Analysis ---")
if shallow_result[0] == 0:
   print("Shallow Copy affected original data")
else:
   print("Shallow Copy did NOT affect original")
if deep_result[0] > 0:
   print("Deep Copy remained independent")
else:
   print("Deep Copy affected original")
print("\n--- Example Demonstration ---")
example_difference()
print("\nExplanation:")
print("Shallow copy shares nested dictionaries, so modifying inner values changes original data.")
print("Deep copy creates separate nested objects, so original data remains unchanged.")
