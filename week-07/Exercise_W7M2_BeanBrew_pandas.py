# Programmer: Arash
# Date: 11-25-2026
# Purpose: Clean and summarize coffee orders with pandas
# Instructor: Deodat Sharma

import pandas as pd
import numpy as np

print("pandas is ready!")


heading = "Task 1.1 Drink prices as a Series"
print(f"\n{heading}\n{'-' * len(heading)}")

drink_prices = [4.75, 4.25, 5.25]
price_series = pd.Series(drink_prices)
print(price_series)
price_series = pd.Series(drink_prices, index=["Latte", "Cold Brew", "Mocha"])
print(price_series)
extra_menu = {"Chai": 4.50, "Espresso": 3.00}
extra_prices = pd.Series(extra_menu)
print(extra_prices)
print(price_series["Mocha"])


heading = "Task 1.2 Build the stock table"
print(f"\n{heading}\n{'-' * len(heading)}")

stock_counts = {"drink": ["Latte", "Cold Brew", "Mocha"],
                "cups_left": [120, 54, 98]}
stock_table = pd.DataFrame(stock_counts)
print(stock_table)
print(stock_table.to_string())
cup_array = np.array([[120, 54, 98]])
print(pd.DataFrame(cup_array))  # The columns get numbers when no names are given


heading = "Task 1.3 Add sizes and sample data"
print(f"\n{heading}\n{'-' * len(heading)}")

stock_table.insert(1, "size", ["M", "L", "M"])
print(stock_table)
sample_sales = pd.DataFrame(np.arange(6).reshape((3, 2)),
                            index=["Back Bay", "Kendall", "Seaport"],
                            columns=["Mon", "Tue"])
print(sample_sales)


heading = "Task 1.4 Select rows by label and position"
print(f"\n{heading}\n{'-' * len(heading)}")

store_cups = pd.DataFrame({"Mon": [120, 98, 143], "Tue": [135, 110, 128]},
                          index=["Back Bay", "Kendall", "Seaport"])
print(store_cups)
print(store_cups["Kendall":])
print(store_cups.loc["Seaport"])
print(store_cups.loc[["Back Bay", "Seaport"]])
print(store_cups.iloc[0])
# Prediction: loc[0] fails because 0 is not a store label.
# print(store_cups.loc[0])  # KeyError: 0
store_cups.loc["Fenway"] = [88, 91]
print(store_cups)


heading = "Task 1.5 Read the orders file"
print(f"\n{heading}\n{'-' * len(heading)}")

online_orders = pd.read_csv("bb_orders.csv")
print(online_orders)
print(pd.options.display.max_rows)


heading = "Task 1.6 Explore the orders"
print(f"\n{heading}\n{'-' * len(heading)}")

print(online_orders.head(3))
print(online_orders.tail(2))
print(online_orders.describe())
online_orders.info()
print(online_orders["store"].value_counts())
# qty has -2 and 50. The price and notes columns have missing values.
# Kendall has two spellings, so it shows up as two stores.


heading = "Task 1.7 Change text into dates"
print(f"\n{heading}\n{'-' * len(heading)}")

print(online_orders["order_date"].dtype)
# Prediction: dt.month fails because these dates are still text.
# print(online_orders["order_date"].dt.month)  # AttributeError: needs datetimelike values
online_orders["order_date"] = pd.to_datetime(online_orders["order_date"])
print(online_orders["order_date"].dtype)
march_orders = online_orders[online_orders["order_date"] >= "2026-03-01"]
print(len(march_orders))


heading = "Task 2.1 Remove notes and duplicate orders"
print(f"\n{heading}\n{'-' * len(heading)}")

online_orders = online_orders.drop("notes", axis=1)
print(online_orders.shape)
print(online_orders.duplicated().sum())
# Prediction: None, because inplace changes the table itself.
duplicate_result = online_orders.drop_duplicates(inplace=True)
print(duplicate_result)
print(online_orders.shape)
print(len(online_orders.dropna()))
# dropna would keep 14 rows, but the missing Mocha price can be filled instead.


heading = "Task 2.2 Filter orders"
print(f"\n{heading}\n{'-' * len(heading)}")

large_orders = online_orders[online_orders["qty"] >= 4]
print(large_orders)
back_bay_orders = online_orders[online_orders["store"] == "Back Bay"]
print(len(back_bay_orders))
back_bay_large = online_orders[(online_orders["store"] == "Back Bay") &
                               (online_orders["qty"] >= 2)]
print(back_bay_large[["order_id", "qty"]])
# The order for 50 cups looks much bigger than the others.


heading = "Task 2.3 Fix store names and the missing price"
print(f"\n{heading}\n{'-' * len(heading)}")

print(online_orders["store"].value_counts())
online_orders.replace({"store": {"Kendall Sq": "Kendall Square"}}, inplace=True)
print(online_orders["store"].value_counts())
online_orders["price"] = online_orders.price.fillna(5.25)
print(online_orders.loc[8])


heading = "Task 2.4 Fix or drop bad quantities"
print(f"\n{heading}\n{'-' * len(heading)}")

online_orders.loc[12, "qty"] = 5  # The correct amount was confirmed as 5
for row_label in online_orders.index:
    if online_orders.loc[row_label, "qty"] <= 0:
        online_orders.drop(row_label, inplace=True)  # The real quantity is unknown
print(online_orders[["order_id", "qty"]].tail(4))
print(online_orders.shape)


heading = "Task 2.5 Add revenue"
print(f"\n{heading}\n{'-' * len(heading)}")

print(online_orders["qty"].sum())
print(online_orders.qty.max())
online_orders["revenue"] = online_orders["qty"] * online_orders["price"]
print(online_orders[["drink", "qty", "price", "revenue"]].head())


heading = "Task 3.1 Revenue summaries"
print(f"\n{heading}\n{'-' * len(heading)}")

order_revenue = online_orders["revenue"]
print(order_revenue.sum())
print(order_revenue.count())
print(round(order_revenue.mean(), 2))
print(order_revenue.median())
print(order_revenue.min(), order_revenue.max())
print(online_orders.aggregate({"qty": ["sum", "mean"],
                               "revenue": ["sum", "max"]}))


heading = "Task 3.2 Group sales by store and drink"
print(f"\n{heading}\n{'-' * len(heading)}")

store_revenue = online_orders.groupby("store")["revenue"].sum()
print(store_revenue)
drink_totals = online_orders.groupby("drink")[["qty"]].sum()
print(drink_totals)
print(online_orders.groupby("store")["qty"].mean().round(2))


heading = "Task 3.3 Sort the sales"
print(f"\n{heading}\n{'-' * len(heading)}")

print(store_revenue.sort_values(ascending=False))
highest_orders = online_orders.sort_values("revenue", ascending=False)
print(highest_orders[["order_id", "store", "revenue"]].head(3))
print(drink_totals.sort_index(ascending=False))
# Sorting keeps the original row labels.


heading = "Task 3.4 Rank stores and drinks"
print(f"\n{heading}\n{'-' * len(heading)}")

print(store_revenue.rank(ascending=False))
drink_totals["rank"] = drink_totals["qty"].rank(ascending=False)
print(drink_totals)
# Cold Brew and Mocha tie at rank 2.5. Ranking gives places without moving rows.


heading = "Task 3.5 Merge drink costs"
print(f"\n{heading}\n{'-' * len(heading)}")

drink_menu = pd.DataFrame({
    "drink": ["Chai", "Cold Brew", "Espresso", "Latte", "Mocha"],
    "cost": [1.40, 1.10, 0.90, 1.60, 1.90]})
drink_costs = pd.merge(drink_menu, drink_totals[["qty"]], on="drink")
drink_costs["total_cost"] = drink_costs["qty"] * drink_costs["cost"]
print(drink_costs)
order_details = pd.merge(online_orders, drink_menu, on="drink")
print(order_details.shape)
# Each order gets its drink cost, so there are still 14 rows.


heading = "Task 3.6 Sales by month"
print(f"\n{heading}\n{'-' * len(heading)}")

online_orders["month"] = online_orders["order_date"].dt.month
online_orders["weekday"] = online_orders["order_date"].dt.day_name()
print(online_orders[["order_date", "month", "weekday"]].head(3))
online_orders["order_month"] = online_orders["order_date"].dt.to_period("M")
month_revenue = online_orders.groupby("order_month")["revenue"].sum()
print(month_revenue)


# Reflection 1:
# loc[0] looks for a label named 0, but my labels are store names.
# iloc[0] gets the first row by position. After dropping row 7, I would use
# iloc[7] for the eighth row because positions count from 0.

# Reflection 2:
# inplace=True changes the existing table and returns None.
# If I assigned that result back to online_orders, I would lose the table
# in that variable and it would hold None instead.

# Reflection 3:
# I would fix a value when I know what it should be, like 50 changing to 5.
# If I do not know the real value, dropping it is better than guessing.

# Reflection 4:
# Without cleaning, Seaport would have $251.50 instead of $60.25.
# The 50-cup mistake adds $191.25, so counting first gives the wrong answer.

# Reflection 5:
# dt.month only keeps the month number, so January from two years gets mixed.
# to_period("M") keeps the year too, so each January stays separate.
