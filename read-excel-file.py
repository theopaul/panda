import pandas as pd
import numpy as np

def analyze_excel(file_path):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    
    # Display basic information about the DataFrame
    print("Basic Information:")
    df.info()
    
    # Display the first few rows of the DataFrame to understand what the data looks like
    print("\nFirst 5 Rows:")
    print(df.head())
    
    # Display statistics for numeric columns
    print("\nStatistics for Numeric Columns:")
    print(df.describe())
    
    # Display column names
    print("\nColumn Names:")
    print(df.columns.tolist())
    
    # Check for missing values in each column
    print("\nMissing Values per Column:")
    print(df.isnull().sum())
    
    # Check for duplicate rows
    print("\nNumber of Duplicate Rows:")
    print(df.duplicated().sum())

    # Correlation matrix for numeric columns (if necessary)
    if input("Do you want to see the correlation matrix? (yes/no): ").strip().lower() == 'yes':
        numeric_df = df.select_dtypes(include=[np.number])
        print("\nCorrelation Matrix:")
        print(numeric_df.corr())

# Provide the path to your Excel file
file_path = "/Users/theosantana/Documents/python/panda/electronic-contacts.xlsx"
analyze_excel(file_path)
