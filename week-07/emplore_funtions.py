# Import pandas and NumPy.
import pandas as pd
import numpy as np

# Create a Series with numbers and one missing value.
numbers = pd.Series([10, 20, 30, 20, np.nan])

# Show the original Series.
print("Original Series:")
print(numbers)

# Calculate basic statistics.
print("\nStatistics:")
print("Sum:", numbers.sum())
print("Mean:", numbers.mean())
print("Median:", numbers.median())
print("Minimum:", numbers.min())
print("Maximum:", numbers.max())

# Show the first three values.
print("\nFirst three values:")
print(numbers.head(3))

# Show which values are missing.
print("\nMissing values:")
print(numbers.isnull())


# Replace missing values with 0.
filled_numbers = numbers.fillna(0)
print("\nNew Series, missin value replace by 0:")
print(filled_numbers)

# Sort values from smallest to largest.
print("\nSorted values:")
print(numbers.sort_values())

# Count each value in the original Series.
print("\nValue counts in orginal series:")
print(numbers.value_counts())

# Count each value in the filled Series.
print("\nValue counts in new Series")
print(filled_numbers.value_counts())

