import pandas as pd

# Load dataset
df = pd.read_csv("data/amazon.csv")

# Show first 5 rows
print(df.head())

# Show dataset info
print(df.info())