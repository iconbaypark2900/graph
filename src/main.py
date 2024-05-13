# main.py
import pandas as pd
from src.data_generation.generate_users import generate_users
from src.data_generation.generate_products import generate_products
from src.data_generation.generate_transactions import generate_transactions
from src.graph_construction.build_graph import build_complete_graph
from src.analysis.query_graph import get_transactions_by_user, get_products_by_transaction
from src.analysis.graph_algorithms import calculate_centrality, detect_communities
from src.visualization.visualize_graph import draw_graph_with_matplotlib, draw_graph_with_plotly

def main():
    # Step 1: Generate Synthetic Data
    print("Generating synthetic data...")
    users_df = generate_users(1000)
    products_df = generate_products(100)
    transactions_df = generate_transactions(10000, 1000, 100)
    
    # Step 2: Build the Knowledge Graph
    print("Building the knowledge graph...")
    G = build_complete_graph(users_df, products_df, transactions_df)
    
    # Step 3: Query the Graph
    print("Querying the graph...")
    user_transactions = get_transactions_by_user(G, 1)  # Example: Get transactions for user with ID 1
    print("Transactions for User 1:", user_transactions)
    
    transaction_products = get_products_by_transaction(G, 100)  # Example: Get products for transaction with ID 100
    print("Products for Transaction 100:", transaction_products)
    
    # Step 4: Perform Graph Analysis
    print("Analyzing the graph...")
    centrality = calculate_centrality(G)
    print("Centrality:", centrality)
    
    communities = detect_communities(G)
    print("Communities detected:", list(communities))
    
    # Step 5: Visualize the Graph
    print("Visualizing the graph...")
    draw_graph_with_matplotlib(G)
    draw_graph_with_plotly(G)

if __name__ == "__main__":
    main()