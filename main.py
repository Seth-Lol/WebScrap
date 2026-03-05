import pandas as pd

# Create a simple table of data (called a DataFrame)
data = {
    "Names": ["Alice", "Bob", "Charlie"],
    "Ages": [25, 30, 35]
}

df = pd.DataFrame(data)

print("Pandas is working! Here is your data:")
print(df)