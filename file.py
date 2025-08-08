import pandas as pd
import numpy as np

#set random seed for responsability
np.random.seed(42)

#generate product.csv
n_products = 1000
products = pd.DataFrame({
    'product_id': range(1, n_products + 1),
    'category': np.random.choice(['Clothing', 'Shoes', 'Accessoires'], n_products),
    'product_name': ['Product_' + str(i) for i in range(n_products)],
    'selling_price': np.random.uniform(10, 200, n_products).round(2),
    'cost_price': np.random.uniform(5, 100, n_products).round(2), 
    'stock': np.random.randint(0, 500, n_products)
})
products.to_csv('data/products.csv', index=False)

#Generate customers.csv
n_customers = 5000
customers = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),
    'gender': np.random.choice(['Male', 'Femmale'], n_customers),
    'age': np.random.randint(18, 70, n_customers),
    'city': np.random.choice(['Douala', 'Yaounde', 'Buea', 'Bamenda', 'Bertoua', 'Bafoussam', 'Dschang'], n_customers),
    'country': 'Cameroon',
    'signup_date': pd.to_datetime('2022-01-01') + pd.to_timedelta(np.random.randint(0, 730, n_customers), unit='days')
})
customers.to_csv('data/customers.csv', index=False)

#Generate marketing.csv
n_campaigns = 2000
marketing = pd.DataFrame({
    'campaign_id': range(1, n_campaigns + 1),
    'channel': np.random.choice(['Facebook', 'Instagram', 'TikTok', 'Google Ads'], n_campaigns),
    'cost': np.random.uniform(100, 5000, n_campaigns).round(2),
    'impressions': np.random.randint(1000, 1000000, n_campaigns),
    'clicks': np.random.randint(100, 150000, n_campaigns),
    'conversions': np.random.randint(0, 10000, n_campaigns),
    'date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 730, n_campaigns), unit='days')
})
marketing.to_csv('data/marketing.csv', index=False)

#Generate Orders.csv
n_orders = 100000
orders = pd.DataFrame({
    'order_id': range(1, n_orders + 1),
    'order_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 730, n_orders), unit='days'),
    'product_id': np.random.randint(1, n_products + 1, n_orders),
    'customer_id': np.random.randint(1, n_customers + 1, n_orders),
    'channel': np.random.choice(['Facebook', 'Instagram', 'TikTok', 'Google Ads'], n_orders),
    'quantity': np.random.randint(1, 10, n_orders),
    'unit_price': np.random.uniform(10, 200, n_orders).round(2),
    'status': np.random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'], n_orders),
    'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer'], n_orders),
    'total_amount': lambda x: (x['quantity'] * x['unit_price']).round(2)
})
orders.to_csv('data/orders.csv', index=False)