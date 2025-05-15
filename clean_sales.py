import pandas as pd

# Read the CSV file
df = pd.read_csv("sales_data.csv")

# Drop blank rows
df.dropna(inplace=True)

# Add a new column: Total = Quantity × Price
df["Total"] = df["Quantity"] * df["Price"]

# Save to Excel
df.to_excel("output_cleaned_sales.xlsx", index=False)

print("File cleaned and saved as output_cleaned_sales.xlsx")
