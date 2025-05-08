import pandas as pd

#  Read file CSV
df = pd.read_csv('Warehouse_and_Retail_Sales.csv')

# 2. Overview
print("Number of rows and columns:", df.shape)
print("nData types:")
print(df.dtypes)

# 3. Check missing values
print("nNumber of missing values per column:")
print(df.isnull().sum())

# 4. Check for redundancy
print("nNumber of duplicate rows:")
print(df.duplicated().sum())

# 5. Data Cleanup

# Delete duplicate rows
df = df.drop_duplicates()

# Dealing with null values (examples):
# Delete rows with missing values
df=df.dropna()

# or substitute missing values with a certain value (example: average of numbers)
# df['column_name'] = df['column_name'].fillna(df['column_name'].mean())

# Change data type if necessary (example: convert column to integer)
# df['column_name'] = df['column_name'].astype(int)

# View the final look after cleaning
print("nAfter cleaning:")
print("Number of rows and columns:", df.shape)

print(df.dtypes)