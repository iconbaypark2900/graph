# generate_users.py
import pandas as pd
from faker import Faker

def generate_users(num_users=1000):
    fake = Faker()
    users = [{'user_id': i,
              'name': fake.name(),
              'email': fake.email(),
              'address': fake.address()} for i in range(num_users)]
    return pd.DataFrame(users)

if __name__ == "__main__":
    users_df = generate_users()
    print(users_df.head())
