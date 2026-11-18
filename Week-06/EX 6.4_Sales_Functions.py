# Purpose: Analyze monthly sales.
employees = ["John", "Sarah", "Michael", "Jennifer", "David"]
sales = [5200, 6800, 4500, 7200, 5800]


def calculate_total(sales):
    total = 0
    for amount in sales:
        total += amount
    return total


def calculate_average(total, number_of_employees):
    return total / number_of_employees


def evaluate_performance(amount):
    if amount >= 7000:
        return "Excellent"
    elif amount >= 6000:
        return "Good"
    elif amount >= 5000:
        return "Average"
    else:
        return "Needs Improvement"


def find_highest_sales(sales):
    highest = sales[0]
    for amount in sales:
        if amount > highest:
            highest = amount
    return highest


def calculate_commission(amount, rate):
    return amount * rate


def above_average(sales, average):
    count = 0
    for amount in sales:
        if amount > average:
            count += 1
    return count


def calculate_annual_sales(amount):
    return amount * 12


total = calculate_total(sales)
print(f"Total Monthly Sales: ${total:,.2f}\n")

average = calculate_average(total, len(employees))
print(f"Average Sales per Employee: ${average:,.2f}\n")

print("EMPLOYEE SALES PERFORMANCE")
print("-" * 26)
for i in range(len(employees)):
    performance = evaluate_performance(sales[i])
    print(f"{employees[i]}: ${sales[i]:,.2f} - {performance}")
print()

highest_sales = find_highest_sales(sales)
print(f"Highest Sales Amount: ${highest_sales:,.2f}\n")

commission = calculate_commission(5200, 0.05)
print(f"John's Commission: ${commission:,.2f}\n")

print("EMPLOYEE SALES SUMMARY")
print("-" * 54)
print(f"{'Employee':<10} {'Sales':<12} {'Performance':<20} {'Commission':<10}")
print("-" * 54)
for i in range(len(employees)):
    performance = evaluate_performance(sales[i])
    commission = calculate_commission(sales[i], 0.05)
    sales_text = f"${sales[i]:,.2f}"
    commission_text = f"${commission:,.2f}"
    print(f"{employees[i]:<10} {sales_text:<12} {performance:<20} {commission_text}")


def calculate_commission(amount):
    if amount >= 7000:
        rate = 0.10
    else:
        rate = 0.05
    return amount * rate


print("\n--- Challenge 1: Sales Bonus ---")
print(f"Jennifer's Commission: ${calculate_commission(7200):,.2f}")
print(f"John's Commission: ${calculate_commission(5200):,.2f}")

print("\n--- Challenge 2: Employees Above Average ---")
print(f"Employees Above Average: {above_average(sales, average)}")

print("\n--- Challenge 3: Projected Annual Sales ---")
for i in range(len(employees)):
    annual_sales = calculate_annual_sales(sales[i])
    print(f"{employees[i]}: ${annual_sales:,.2f}")