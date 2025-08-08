import pandas as pd

# ---------------------------
# 1. Chargement des datasets
# ---------------------------
orders = pd.read_csv('data/orders.csv')
customers = pd.read_csv('data/customers.csv')
products = pd.read_csv('data/products.csv')
marketing = pd.read_csv('data/marketing.csv')

# ---------------------------
# 2. Nettoyage rapide
# ---------------------------

# -- Convertir les dates
orders['order_date'] = pd.to_datetime(orders['order_date'])
customers['signup_date'] = pd.to_datetime(customers['signup_date'])
marketing['date'] = pd.to_datetime(marketing['date'])

# -- Vérifier colonnes manquantes
print("Missing values:\n", orders.isnull().sum())
print(customers.isnull().sum())
print(products.isnull().sum())
print(marketing.isnull().sum())

# -- Exemple de remplacement valeurs manquantes si besoin :
# orders.fillna({'status':'Unknown'}, inplace=True)

# ---------------------------
# 3. Merge des datasets
# ---------------------------

df = orders.merge(customers, how='left', on='customer_id')
df = df.merge(products, how='left', on='product_id')

# ⚠️ Le fichier marketing ne se merge pas directement sur les commandes :
# On le gardera à part pour calculer plus tard le ROI par canal marketing.

# ---------------------------
# 4. Création de variables utiles pour KPI
# ---------------------------

df['revenue'] = df['unit_price'] * df['quantity']
df['month'] = df['order_date'].dt.to_period('M')

# ---------------------------
# 5. Export de la table finale 
# ---------------------------

df.to_csv('final_table.csv', index=False)
print("Fichier final_table.csv generate with success !")
