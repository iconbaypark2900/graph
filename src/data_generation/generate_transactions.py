# generate_transactions.py
import pandas as pd
from faker import Faker
import random
import numpy as np

def generate_transactions(num_transactions=10000, num_users=1000, num_products=100):
    fake = Faker()
    transaction_types = ['Deposit', 'Withdrawal', 'Payment', 'Transfer']
    transactions = [{'transaction_id': i,
                     'user_id': random.randint(1, num_users),
                     'product_id': random.randint(1, num_products),
                     'transaction_type': random.choice(transaction_types),
                     'amount': np.random.randint(100, 5000),
                     'date': fake.date_between(start_date='-2y', end_date='today')}
                    for i in range(num_transactions)]
    return pd.DataFrame(transactions)

if __name__ == "__main__":
    transactions_df = generate_transactions()
    print(transactions_df.head())
