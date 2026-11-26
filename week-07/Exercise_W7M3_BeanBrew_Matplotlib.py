# Programmer: Arash
# Date: 11-25-2026
# Purpose: Practice line, bar, scatter, histogram and pie charts
# Instructor: Deodat Sharma

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

print("Matplotlib is ready!")


heading = "Task 1.1 My first line graphs"
print(f"\n{heading}\n{'-' * len(heading)}")

trial_days = np.array([1, 7])
trial_cups = np.array([2, 14])
plt.plot(trial_days, trial_cups)
plt.title("Cold Brew Trial")
plt.xlabel("Day")
plt.ylabel("Cups Sold")
plt.show()

week_cups = np.array([112, 98, 105, 120, 138, 162, 151])
# Prediction: without x values, the days start at 0 and finish at 6.
plt.plot(week_cups)
plt.title("Cups Sold During the Week")
plt.xlabel("Day Position")
plt.ylabel("Cups Sold")
plt.show()


heading = "Task 1.2 Plot a pandas table"
print(f"\n{heading}\n{'-' * len(heading)}")

monthly_cups = pd.DataFrame({
    "month": [1, 2, 3, 4, 5, 6],
    "cups_sold": [3120, 2890, 3410, 3655, 3980, 4210]})
plt.title("Total Cups Sold from January to June")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.plot(monthly_cups["month"], monthly_cups["cups_sold"])
plt.show()


heading = "Task 1.3 Compare markers and lines"
print(f"\n{heading}\n{'-' * len(heading)}")

plt.plot(monthly_cups["month"], monthly_cups["cups_sold"], marker="o")
plt.title("Monthly Cups with a Line and Dots")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.show()

plt.plot(monthly_cups["month"], monthly_cups["cups_sold"], "o")
plt.title("Monthly Cups with Dots Only")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.show()


heading = "Task 1.4 Style the markers"
print(f"\n{heading}\n{'-' * len(heading)}")

plt.plot(monthly_cups["month"], monthly_cups["cups_sold"],
         marker="D", ms=10, mfc="gold", mec="saddlebrown")
plt.title("Monthly Cups with Gold Diamonds")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.show()


heading = "Task 1.5 Use the format shortcut"
print(f"\n{heading}\n{'-' * len(heading)}")

plt.plot(monthly_cups["month"], monthly_cups["cups_sold"], "s--g")
plt.title("Monthly Cups with Green Squares")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.show()

# Prediction: the full word brown will not work inside the format string.
# plt.plot(monthly_cups["month"], monthly_cups["cups_sold"], "o:brown")
# ValueError: the format string has two color symbols, b and r.
plt.plot(monthly_cups["month"], monthly_cups["cups_sold"], "o:", color="brown")
plt.title("Monthly Cups with Brown Circles")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.show()


heading = "Task 1.6 Compare two stores"
print(f"\n{heading}\n{'-' * len(heading)}")

back_bay_cups = np.array([1050, 960, 1120, 1190, 1280, 1330])
seaport_cups = np.array([1010, 940, 1150, 1240, 1370, 1480])
plt.plot(monthly_cups["month"], back_bay_cups, lw=4, c="seagreen", label="Back Bay")
plt.plot(monthly_cups["month"], seaport_cups, ls="--", marker="o",
         c="#D98E1F", label="Seaport")
plt.title("Back Bay and Seaport Cup Sales")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.legend()
plt.show()


heading = "Task 1.7 Make a wider chart"
print(f"\n{heading}\n{'-' * len(heading)}")

print(plt.rcParams["figure.figsize"])
kendall_cups = np.array([1060, 990, 1140, 1225, 1330, 1400])
plt.figure(figsize=(10, 4))
plt.plot(monthly_cups["month"], back_bay_cups, lw=4, c="seagreen", label="Back Bay")
plt.plot(monthly_cups["month"], seaport_cups, ls="--", marker="o",
         c="#D98E1F", label="Seaport")
plt.plot(monthly_cups["month"], kendall_cups, c="steelblue", label="Kendall Square")
plt.title("Monthly Cups for All Three Stores")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.legend()
plt.show()


heading = "Task 2.1 Add fonts and a legend"
print(f"\n{heading}\n{'-' * len(heading)}")

title_font = {"color": "darkblue", "size": 15}
label_font = {"family": "serif"}
plt.title("Cups Sold by Store", fontdict=title_font, loc="left")
plt.xlabel("Month", fontdict=label_font)
plt.ylabel("Cups Sold", fontdict=label_font)
plt.plot(monthly_cups["month"], back_bay_cups, lw=4, c="seagreen", label="Back Bay")
plt.plot(monthly_cups["month"], seaport_cups, ls="--", marker="o",
         c="#D98E1F", label="Seaport")
plt.plot(monthly_cups["month"], kendall_cups, c="steelblue", label="Kendall Square")
plt.legend()
plt.show()


heading = "Task 2.2 Add a horizontal grid"
print(f"\n{heading}\n{'-' * len(heading)}")

plt.plot(monthly_cups["month"], monthly_cups["cups_sold"], marker="o")
plt.title("Total Cups Sold Each Month")
plt.xlabel("Month")
plt.ylabel("Cups Sold")
plt.grid(axis="y", color="gray", linestyle="--", linewidth=0.5)
plt.show()


heading = "Task 2.3 Store and drink bar charts"
print(f"\n{heading}\n{'-' * len(heading)}")

store_sales = pd.DataFrame({
    "store": ["Back Bay", "Kendall Square", "Seaport"],
    "revenue": [38.75, 39.00, 60.25]})
plt.bar(store_sales["store"], store_sales["revenue"], color="mediumpurple", width=0.6)
plt.title("Online Revenue by Store, Q1")
plt.xlabel("Store")
plt.ylabel("Revenue ($)")
plt.show()

drink_names = ["Chai", "Cold Brew", "Espresso", "Latte", "Mocha"]
# Prediction: five drinks and four numbers cause a shape mismatch.
# drink_cups = [4, 6, 2, 12]
# plt.barh(drink_names, drink_cups)  # ValueError: shapes (5,) and (4,) do not match
drink_cups = [4, 6, 2, 12, 6]
plt.barh(drink_names, drink_cups, height=0.5)
plt.title("Online Cups Sold by Drink, Q1")
plt.xlabel("Cups Sold")
plt.ylabel("Drink")
plt.show()


heading = "Task 2.4 Temperature and drink sales"
print(f"\n{heading}\n{'-' * len(heading)}")

day_temps = np.array([48, 52, 55, 61, 64, 68, 72, 75, 79, 84])
cold_brew_cups = np.array([22, 25, 31, 38, 41, 50, 57, 60, 68, 74])
latte_cups = np.array([88, 84, 80, 74, 70, 66, 61, 55, 52, 47])
plt.scatter(day_temps, cold_brew_cups, c="teal", label="Cold Brew")
plt.scatter(day_temps, latte_cups, c="chocolate", label="Latte")
plt.title("Daily Drink Sales and Temperature")
plt.xlabel("Temperature (F)")
plt.ylabel("Cups Sold")
plt.legend()
plt.show()
# The teal dots go up as it gets warmer, so cold brew sales increase.
# The brown dots go down, so latte sales decrease on warmer days.


heading = "Task 2.5 Show how busy the cafe was"
print(f"\n{heading}\n{'-' * len(heading)}")

seats_taken = np.array([35, 40, 38, 52, 55, 61, 70, 78, 86, 95])
plt.scatter(day_temps, cold_brew_cups, c=seats_taken, cmap="viridis")
plt.colorbar(label="Seats Taken (%)")
plt.title("Cold Brew Sales and Temperature")
plt.xlabel("Temperature (F)")
plt.ylabel("Cold Brew Cups")
plt.show()


heading = "Task 2.6 Show the wait times"
print(f"\n{heading}\n{'-' * len(heading)}")

np.random.seed(7)
order_waits = np.random.normal(loc=4, scale=1, size=1000)
print(np.round(np.mean(order_waits), 2))
plt.figure(figsize=(10, 6))
plt.hist(order_waits, bins=15, color="skyblue", edgecolor="black")
plt.title("Wait Times for 1,000 Orders")
plt.xlabel("Wait (minutes)")
plt.ylabel("Number of Orders")
plt.grid(axis="y", alpha=0.75)
plt.show()


heading = "Task 2.7 Show each drink share"
print(f"\n{heading}\n{'-' * len(heading)}")

slice_offset = [0, 0, 0, 0.1, 0]
plt.figure(figsize=(8, 5))
plt.pie(drink_cups, startangle=90, explode=slice_offset, autopct="%1.0f%%")
plt.title("Share of Online Cups by Drink, Q1")
plt.legend(drink_names, title="Drink", loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()


heading = "Task 2.8 Put two charts side by side"
print(f"\n{heading}\n{'-' * len(heading)}")

sales_figure, charts = plt.subplots(1, 2, figsize=(12, 5))
charts[0].bar(store_sales["store"], store_sales["revenue"], color="mediumpurple")
charts[0].set_title("Online Revenue by Store")
charts[0].set_xlabel("Store")
charts[0].set_ylabel("Revenue ($)")
charts[1].pie(drink_cups, labels=drink_names, startangle=90)
charts[1].set_title("Share of Cups by Drink")
# Prediction: there is no third chart because there are only two positions.
# charts[2].plot(monthly_cups["month"], monthly_cups["cups_sold"])  # IndexError
plt.show()


heading = "Task 2.9 Save the store revenue chart"
print(f"\n{heading}\n{'-' * len(heading)}")

plt.title("Online Revenue by Store, Q1")
plt.xlabel("Store")
plt.ylabel("Revenue ($)")
plt.bar(store_sales["store"], store_sales["revenue"], color="mediumpurple", width=0.6)
plt.savefig("bb_store_revenue.png", dpi=150)  # Save while the chart is still open
print(os.path.exists("bb_store_revenue.png"))
plt.show()


# Reflection 1:
# Without x values, Matplotlib uses positions starting at 0.
# I would pass np.arange(1, 8) before week_cups to show days 1 through 7.

# Reflection 2:
# The format string only accepts short color codes, so brown does not fit there.
# The shortcut is handy for a simple style like s--g.
# A keyword like color="brown" is clearer when using a full color name.

# Reflection 3:
# The bar charts compare stores and drinks, while the scatter chart shows
# how drink sales change with temperature. The pie shows each drink's share
# of total cups. A monthly pie would hide the changes over time, so a line is better.

# Reflection 4:
# With 5 bins, the bars are wider and hide some of the detail.
# With 60 bins, the bars are narrow and the chart looks more uneven.
# I kept 15 because the overall shape is easier to see.

# Reflection 5:
# Saving after closing the show window can give me a blank picture.
# The chart is closed by then, so I save it before show instead.
