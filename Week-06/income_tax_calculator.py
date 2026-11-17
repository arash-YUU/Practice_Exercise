# Name: Arash
# Date: 11-16-2026
# Description: Calculates estimated income tax based on annual income and number of dependents.

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 2000

print("INCOME TAX CALCULATOR")
print("-" * 40)

gross_annual_income = float(input("Enter gross annual income: "))
dependents = int(input("Enter number of dependents: "))

dependents_deduction = DEPENDENT_DEDUCTION * dependents
total_deduction = STANDARD_DEDUCTION + dependents_deduction
taxable_income = gross_annual_income - total_deduction
estimate_tax = taxable_income * TAX_RATE

print()
print("INCOME TAX SUMMARY")
print("-" * 40)

print(f"{'Gross Income:':<25}{f'${gross_annual_income:,.2f}':>15}")
print(f"{'Standard Deduction:':<25}{f'${STANDARD_DEDUCTION:,.2f}':>15}")
print(f"{'Dependent Deductions:':<25}{f'${dependents_deduction:,.2f}':>15}")
print(f"{'Total Deductions:':<25}{f'${total_deduction:,.2f}':>15}")
print(f"{'Taxable Income:':<25}{f'${taxable_income:,.2f}':>15}")
print(f"{'Tax Rate:':<25}{TAX_RATE:>15.0%}")
print(f"{'Estimated Income Tax:':<25}{f'${estimate_tax:,.2f}':>15}")