import pandas as pd
from datetime import datetime


# Load the CSV file
file_path = 'Mall_Customers.csv'
df = pd.read_csv(file_path)

#Convert the 'Date' column to datetime format
df['date']=pd.to_datetime(df['date'],  dayfirst=True, errors='coerce')
print('converted Date Column to datetime format')
# Print the first few rows of the updated DataFrame to verify the changes
print(df.head())

# Check for missing values
if df.isnull().values.any():
    print("Missing values found in the DataFrame.")
    #Fill Null values with the mean of the column
    df=df.fillna(df.select_dtypes(include='number').mean()) 
    print("replaced null with mean values")
else:
    print("No missing values found in the DataFrame.")
# Remove Duplicates
df=df.drop_duplicates()
print("removed duplicates")
# Standarize text values for gender column with first letter upper case and rest lower case
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.capitalize()
    print("capitalized Gender column")
df.columns=[col.strip().lower().replace(' ','_') for col in df.columns]
print("standardized column names")
# Save the updated DataFrame back to the CSV file
df.to_csv(file_path, index=False)


