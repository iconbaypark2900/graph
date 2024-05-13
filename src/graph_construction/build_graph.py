# build_graph.py
import networkx as nx
import pandas as pd

def create_graph():
    G = nx.DiGraph()
    return G

def add_users_to_graph(G, users_df):
    for idx, row in users_df.iterrows():
        G.add_node(row['user_id'], type='User', name=row['name'], email=row['email'])

def add_products_to_graph(G, products_df):
    for idx, row in products_df.iterrows():
        G.add_node(row['product_id'], type='Product', product_name=row['product_name'], interest_rate=row['interest_rate'])

def add_transactions_to_graph(G, transactions_df):
    for idx, row in transactions_df.iterrows():
        G.add_node(row['transaction_id'], type='Transaction', transaction_type=row['transaction_type'], amount=row['amount'], date=row['date'])
        G.add_edge(row['user_id'], row['transaction_id'], relationship='performed')
        G.add_edge(row['transaction_id'], row['product_id'], relationship='involves')

def build_complete_graph(users_df, products_df, transactions_df):
    G = create_graph()
    add_users_to_graph(G, users_df)
    add_products_to_graph(G, products_df)
    add_transactions_to_graph(G, transactions_df)
    return G

if __name__ == "__main__":
    # Assuming you have the data loaded into pandas DataFrames
    users_df = pd.read_csv('path_to_users.csv')  # Replace path_to_users.csv with actual path
    products_df = pd.read_csv('path_to_products.csv')  # Replace path_to_products.csv with actual path
    transactions_df = pd.read_csv('path_to_transactions.csv')  # Replace path_to_transactions.csv with actual path
    
    graph = build_complete_graph(users_df, products_df, transactions_df)
    print("Graph has been built with", graph.number_of_nodes(), "nodes and", graph.number_of_edges(), "edges.")
