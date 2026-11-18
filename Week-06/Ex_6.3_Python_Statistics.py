# Programmer: Arash
# Date: 11-17-2026
# Purpose: Analyze daily sales statistics.
# Instructor: Deodat Sharma

import statistics

days = [
'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
]

sales = [1250, 1480, 1100, 1650, 1850,
1420, 1700, 1300, 2100, 1950]

print("DAILY SALES REPORT")
print("-" * 20)

average = statistics.mean(sales)
median = statistics.median(sales)
mode = statistics.mode(sales)
std_deviation = statistics.stdev(sales)
total_sale = sum(sales)
lowest_sale = min(sales)
highest_sale = max(sales)

print(f"Total sale: ${total_sale:,.2f}")
print(f"Lowest Sale: ${lowest_sale:,.2f}")
print(f"Highest Sale : ${highest_sale:,.2f}")
print(f"Average: ${average:,.2f}")
print(f"Median: ${median:,.2f}")
print(f"Mode: ${mode:,.2f}")
print(f"Standar deviation: ${std_deviation:,.2f}")
print()

for day, amount in zip(days, sales):
    if amount >= 1800:
        category = "Excellent"
    elif amount >= 1500:
        category = "Good"
    elif amount >= 1200:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(f"{day}: ${amount:,.2f} - {category}")

