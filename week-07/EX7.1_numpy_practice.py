import numpy as np

# Task 1: Import NumPy and create the 3D sales array
# 2 layers (stores) x 2 rows (months) x 3 columns (sales records)
sales = np.array([
    [
        [1200, 1500, 1800],
        [2000, 2200, 2500],
    ],
    [
        [1400, 1600, 1900],
        [2100, 2300, 2600],
    ],
])

 
print("Task 2 - Sales Array:")
print(sales)


print("\nTask 3 - Elements using np.nditer():")
for item in np.nditer(sales):
    print(item)


print("\nTask 4 - Elements using three nested for loops:")
for store in sales:          # outer loop: stores (layers)
    for month in store:      # middle loop: months (rows)
        for record in month: # inner loop: sales records (columns)
            print(record)


total_sales = 0
for record in np.nditer(sales):
    total_sales += int(record)

print(f"\nTask 5 - Total Sales: {total_sales}")

num_records = 0
for _ in np.nditer(sales):
    num_records += 1

average_sales = total_sales / num_records
print(f"Task 6 - Average Sales: {average_sales:.2f}")


highest_sales = None
for record in np.nditer(sales):
    val = int(record)
    if highest_sales is None or val > highest_sales:
        highest_sales = val

print(f"Task 7 - Highest Sales: {highest_sales}")