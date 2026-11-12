
import pandas as pd

# Read the dataset
data = pd.read_csv("dataset.csv")

# Display the first 5 rows
print(data.head())

# Display the number of rows and columns
print(data.shape)

# Check for missing values
print(data.isnull().sum())
