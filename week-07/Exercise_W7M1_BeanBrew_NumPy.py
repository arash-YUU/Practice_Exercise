# Programmer: Arash
# Date: 11-25-2026
# Purpose: Practice NumPy arrays and random sample data
# Instructor: Deodat Sharma

import numpy as np
import pandas as pd

heading = "Task 1.1 Loop through a 2D array"
print(f"\n{heading}\n{'-' * len(heading)}")

# Rows: Back Bay, Kendall Square. Columns: Mon, Tue, Wed.
cups = np.array([[120, 135, 150],
                 [98, 110, 140]])

for row in cups:
    print(row)

for row in cups:
    for value in row:
        print(value)


heading = "Task 1.2 Join and stack the store data"
print(f"\n{heading}\n{'-' * len(heading)}")

seaport = np.array([[143, 128, 161]])
all_stores = np.concatenate((cups, seaport))  # Add the new store as a row
print(all_stores)

thu_fri = np.array([[140, 172], [101, 95], [150, 166]])
week = np.concatenate((all_stores, thu_fri), axis=1)  # Add two columns
print(week)

mon = np.array([120, 98, 143])
tue = np.array([135, 110, 128])

print(np.hstack((mon, tue)))
print(np.vstack((mon, tue)))
print(np.stack((mon, tue), axis=1))


heading = "Task 1.3 Missing data with NaN and None"
print(f"\n{heading}\n{'-' * len(heading)}")

seaport_week = np.array([143, 128, 161, np.nan, 166])
print(seaport_week)
print(seaport_week.dtype)
print(np.sum(seaport_week))

seaport_none = np.array([143, 128, 161, None, 166])
print(seaport_none.dtype)

# Adding 1 will fail because None is not a number.
# print(seaport_none + 1)  # TypeError
print(seaport_week + 1)


heading = "Task 1.4 Split the week into parts"
print(f"\n{heading}\n{'-' * len(heading)}")

days = np.array([140, 152, 138, 160, 171, 199, 185])

# The first half gets 4 days and the second gets 3.
halves = np.array_split(days, 2)
print(halves)
print(halves[1])

by_store = np.array_split(week, 3)
print(by_store[2])


heading = "Task 1.5 Find the slow days"
print(f"\n{heading}\n{'-' * len(heading)}")

TARGET = 150

print(np.where(days < TARGET))
print(np.where(days < TARGET, "below", "met"))
print(np.where(days < TARGET, days + 15, days))  # Only slow days get extra cups


heading = "Task 1.6 Sort and filter the sales"
print(f"\n{heading}\n{'-' * len(heading)}")

print(np.sort(days))
print(days)

codes = np.array(["95", "100", "9", "120"])
# Text sorts as 100, 120, 9, 95 because characters are compared.
print(np.sort(codes))
print(np.sort(week))

busy = days > 160
print(busy)
print(days[busy])


heading = "Task 2.1 Make repeatable random numbers"
print(f"\n{heading}\n{'-' * len(heading)}")

np.random.seed(7)
test_orders = np.random.randint(1, 6, size=(2, 5))
print(test_orders)

tips = np.random.rand(2, 3)
print(tips)


heading = "Task 2.2 Simulate drink sizes"
print(f"\n{heading}\n{'-' * len(heading)}")

np.random.seed(7)
sizes = ["small", "medium", "large"]

# These probabilities total 1.1, which causes a ValueError.
# orders = np.random.choice(sizes, p=[0.3, 0.5, 0.3], size=10)

orders = np.random.choice(sizes, p=[0.2, 0.5, 0.3], size=10)
print(orders)
print(orders[orders == "large"])
print(np.random.choice(sizes))


heading = "Task 2.3 Simulate wait times"
print(f"\n{heading}\n{'-' * len(heading)}")

np.random.seed(7)
waits = np.random.normal(loc=4, scale=1, size=1000)

print(np.round(np.mean(waits), 2))
print(np.round(np.std(waits), 2))

within_1 = waits[np.absolute(waits - 4) < 1]  # Distance from 4, above or below
print(len(within_1))

within_2 = waits[np.absolute(waits - 4) < 2]
print(len(within_2))

heading = "Task 3.1 Shuffle the barista rota"
print(f"\n{heading}\n{'-' * len(heading)}")

np.random.seed(7)
baristas = np.array(["Ana", "Ben", "Cho", "Dev", "Eli"])

print(np.random.permutation(baristas))
print(baristas)

np.random.shuffle(baristas)  # Change the original order
print(baristas)


heading = "Task 3.2 Revenue and cost"
print(f"\n{heading}\n{'-' * len(heading)}")

mon_cups = np.array([120, 98, 143])
avg_price = np.array([4.50, 4.25, 4.75])

revenue = np.multiply(mon_cups, avg_price)
print(revenue)

cost = np.array([310, 260, 380])
print(np.subtract(revenue, cost))  # Revenue minus costs gives profit
print(np.divmod(mon_cups, 25))  # Full sleeves and cups left over
print(np.absolute(np.array([-12, 5, -3])))


heading = "Task 3.3 Five ways to round"
print(f"\n{heading}\n{'-' * len(heading)}")

changes = np.array([-2.7, -0.5, 0.5, 1.5, 2.5, 3.46])

# Prediction: 0.5 becomes 0, 1.5 becomes 2, and 2.5 becomes 2.
# Halfway values round to the nearest even number.
print(np.trunc(changes))
print(np.fix(changes))
print(np.floor(changes))
print(np.ceil(changes))
print(np.round(changes))
print(np.round(changes, 1))

# For -2.7, trunc gives -2 but floor gives -3 because floor rounds down.


heading = "Task 3.4 Totals and running totals"
print(f"\n{heading}\n{'-' * len(heading)}")

print(week)
print(np.sum(week))

# Prediction: axis 1 gives 3 store totals, and axis 0 gives 5 day totals.
print(np.sum(week, axis=1))
print(np.sum(week, axis=0))
print(np.cumsum(days))


heading = "Task 3.5 Growth and day-to-day change"
print(f"\n{heading}\n{'-' * len(heading)}")

growth = np.array([1.10, 1.05, 1.20])

print(np.round(np.prod(growth), 3))
print(np.round(np.cumprod(growth), 3))
print(np.diff(days))
print(np.diff(days, n=2))


# Reflection 1:
# axis=0 adds the rows together, so I get 5 numbers, one for each day.
# axis=1 adds across each row, so I get 3 numbers, one for each store.

# Reflection 2:
# I would use np.nan because the number is missing, not zero.
# None causes an error when doing math, and 0 would make the total look correct even though a day is missing.

# Reflection 3:
# The numbers are stored as text, so Python compares the characters instead of the number values.
# I would change them to integers first, then sort them.

# Reflection 4:
# Using the same seed gives me the same numbers each time, so it is easier to check my work.
# I would not use these random numbers for passwords because they are not secure.

# Reflection 5:
# I would use np.divmod(143, 25) to find the full sleeves and the cups left over.
# It gives 5 full sleeves and 18 extra cups, so I would need to order 6 sleeves.
# round() could round down in other cases and leave me without enough cups.
