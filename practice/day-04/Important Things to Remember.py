import pandas as pd 
df = pd.read_excel("pandas_filtering_sorting_practice.xlsx")

# One condition
df[df["Age"] > 25]

# AND
df[('condition1') & ('condition2')]

# OR
df[('condition1') | ('condition2')]

# Multiple values
df[df["Department"].isin(["IT", "Finance"])]

# Between values
df[df["Age"].between(25, 30)]

# Text contains
df[df["Name"].str.contains("Khan", case=False, na=False)]

# Sort low → high
df.sort_values("Salary")

# Sort high → low
df.sort_values("Salary", ascending=False)

# Sort multiple columns
df.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False]
)

# Reset index
df.reset_index(drop=True)

# Save to Excel
df.to_excel("output.xlsx", index=False)