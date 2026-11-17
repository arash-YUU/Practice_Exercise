monthly_sales = [1200.50, 1500.75, 1100.00, 1800.25, 1400.00, 1650.50]
months = ["January", "February", "March", "April", "May", "June"]

for index, month in enumerate(months, start=1):
    print(f"Month {index}: {month}")

for index, sales in enumerate(monthly_sales, start=1):
    print(f"Month {index} Sales: ${sales:,.2f}")