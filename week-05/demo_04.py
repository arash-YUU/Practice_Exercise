meal_cost = float(input("Enter the meal cost: "))
tip = float(meal_cost * 0.20)
tax = float(meal_cost * 0.0825)
total_cost = meal_cost + tip + tax

print("------Meal Cost Breakdown---------")
print(f"{"Meal Cost:":<15}${total_cost:6.2f}")
print(f"{"Tip (20%):":<15}${tip:6.2f}")
print(f"{"Tax (8.25%):":<15}${tax:6.2f}")
print("------------------------------")
print(f"{"Total Cost:":<15}${total_cost:6.2f}")