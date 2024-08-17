import pandas as pd

# Sample dataset
data = {
    'Transaction_ID': [1, 2, 3, 4, 5],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Quantity': [10, 5, 2, 8, 7],
    'Price_per_Unit': [100, 200, 100, 300, 200]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

def calculate_total_revenue(df):
    df['Total_revenue'] = df['Quantity'] * df['Price_per_Unit']
    total_revenue = df['Total_revenue'].sum()
    return total_revenue


# Function to calculate the average revenue per transaction
def calculate_average_revenue(df):
    df['Revenue'] = df['Quantity'] * df['Price_per_Unit']
    average_revenue = df['Revenue'].mean()
    return average_revenue

total_revenue = calculate_total_revenue(df)
print(total_revenue)

# Calculate and print average revenue per transaction
average_revenue = calculate_average_revenue(df)
print(average_revenue)
