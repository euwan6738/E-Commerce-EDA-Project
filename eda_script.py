import pandas as pd
import numpy as np

# 1. Load Data
# Simulated based on your project dataset
data = {
    "OrderID": ["ORD2000", "ORD2000", "ORD2000", "ORD2000", "ORD2000"],
    "Date": ["2023-01-15", "2024-08-22", "2024-02-20", "2023-10-10", "2025-05-12"],
    "CustomerID": ["C72649", "C75739", "C81728", "C33540", "C81840"],
    "Product": ["Monitor", "Phone", "Tablet", "Chair", "Printer"],
    "Quantity": [5, 2, 5, 1, 4],
    "UnitPrice": [570.62, 151.35, 550.68, 273.19, 626.01],
    "TotalPrice": [2853.10, 302.70, 2753.40, 273.19, 2504.04]
}
df = pd.DataFrame(data)

# 2. Data Diagnostics (Five-Number Summary)
print("--- DATA COMPLETENESS CHECK ---")
print(df.isnull().sum())
print("\n--- FIVE-NUMBER SUMMARY ---")
print(df.describe())

# 3. Outlier Detection (IQR Method)
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['TotalPrice'] < lower_bound) | (df['TotalPrice'] > upper_bound)]
print(f"\n--- TRANS-ANOMALIES DETECTED (IQR) ---")
print(outliers if not outliers.empty else "No extreme transaction anomalies detected.")

# 4. Correlation Clues
print("\n--- CORRELATION MATRIX ---")
numeric_df = df.select_dtypes(include=[np.number])
print(numeric_df.corr())