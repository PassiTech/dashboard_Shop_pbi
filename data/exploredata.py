import pandas as pd

orders_path = 'orders.csv'
customers_path = 'customers.csv'
products_path = 'products.csv'
marketing_path = 'marketing.csv'

def explore_dataset(df, name):

    # Display basic information about each dataset
    print(f"--- Quick dataset exploration: {name} ---\n")
    print(f"Dimensions: {df.shape}")
    print("\nColumn and type info:")
    print(df.info())
    print("\nPreview (first 5 rows):")
    print(df.head())
    print("\nDescriptive statistics (numeric columns):")
    print(df.describe())
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print("\n")

orders = pd.read_csv(orders_path)
customers = pd.read_csv(customers_path)
products = pd.read_csv(products_path)
marketing = pd.read_csv(marketing_path)

#exploration quickly
explore_dataset(orders, 'Orders')
explore_dataset(customers, 'Customers')
explore_dataset(products, 'Products')
explore_dataset(marketing, 'Marketing')