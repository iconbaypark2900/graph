# generate_products.py
import pandas as pd
import random

def generate_products(num_products=100):
    product_types = ['Savings Account', 'Checking Account', 'Credit Card', 'Investment Fund']
    products = [{'product_id': i,
                 'product_name': random.choice(product_types) + ' ' + str(i),
                 'interest_rate': round(random.uniform(0.01, 0.05), 4) if 'Account' in product_types else None}
                for i in range(num_products)]
    return pd.DataFrame(products)

if __name__ == "__main__":
    products_df = generate_products()
    print(products_df.head())
