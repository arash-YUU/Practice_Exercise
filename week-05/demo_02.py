item1 = 25.75
item2 = 45.67
item3 = 45.75
item4 = 55.75
item5 = 45.60

Subtotal = item1 + item2 + item3 + item4 + item5
tax = Subtotal * 0.07
total = Subtotal + tax

print(f"Sub-Total = ${Subtotal:.2f}")
print(f"       Tax = ${tax:.2f}")
print(f"Total Cost = ${total:.2f}")
