employee_name = input("What is you name: ")
employee_score = int(input("what is you performance score: "))

print()
if employee_score >= 80:
    category = "Excellent Performance"
else:
    category = "Needs Imporvemnts"

print(f"Performacne: {category}")
print(f"Score: {employee_score}")