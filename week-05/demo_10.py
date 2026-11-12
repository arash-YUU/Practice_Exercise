employee_name = input("What is your name: ")
employee_score = int(input("What is your performance score: "))

if employee_score >= 90:
  category = "Outstanding"
elif employee_score >= 80:
  category = "Exceeds Expectations"
elif employee_score >= 70:
  category = "Meets Expectations"
elif employee_score >= 60:
  category = "Below Expectations"
else:
  category = "Unsatisfactory"

print(f"Employee Name: {employee_name}")
print(f"Performance Score: {employee_score}")
print(f"Rating: {category}")