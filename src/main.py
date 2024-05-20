# main.py
import pandas as pd
import logging
import networkx as nx
import matplotlib.pyplot as plt
from data_generation.generate_users import generate_users
from data_generation.generate_products import generate_products
from data_generation.generate_transactions import generate_transactions
from graph_construction.build_graph import build_complete_graph
from analysis.query_graph import get_transactions_by_user, get_products_by_transaction
from analysis.graph_algorithms import calculate_centrality, detect_communities
from visualization.visualize_graph import draw_graph_with_matplotlib, draw_graph_with_plotly
from visualization.visualize_graph import batch_process_graph

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Step 1: Generate Synthetic Data
    logging.info("Generating synthetic data...")
    users_df = generate_users(1000)
    products_df = generate_products(100)
    transactions_df = generate_transactions(10000, 1000, 100)
    
    # Sample data for visualization
    sample_users_df = users_df.sample(n=50)  # Adjust n as needed
    sample_products_df = products_df.sample(n=5)
    sample_transactions_df = transactions_df.sample(n=125)

    # Step 2: Build the Knowledge Graph
    logging.info("Building the knowledge graph...")
    G = build_complete_graph(sample_users_df, sample_products_df, sample_transactions_df)
    
    # Log the size of the graph
    logging.info(f"Number of nodes: {G.number_of_nodes()}")
    logging.info(f"Number of edges: {G.number_of_edges()}")

    # Step 3: Query the Graph
    logging.info("Querying the graph...")
    user_transactions = get_transactions_by_user(G, 1)
    logging.info(f"Transactions for User 1: {user_transactions}")
    
    transaction_products = get_products_by_transaction(G, 100)
    logging.info(f"Products for Transaction 100: {transaction_products}")
    
    # Step 4: Perform Graph Analysis
    logging.info("Analyzing the graph...")
    centrality = calculate_centrality(G)
    logging.info(f"Centrality: {centrality}")
    
    communities = detect_communities(G)
    logging.info(f"Communities detected: {list(communities)}")
    
    # Optional: Simple Visualization for Debugging
    logging.info("Performing simple visualization for debugging...")
    pos = nx.spring_layout(G, scale=2)  # Use a simple layout
    community_colors = {node: cid for cid, community in enumerate(communities) for node in community}
    node_colors = [community_colors[node] if node in community_colors else 1 for node in G.nodes()]
    nx.draw(G, pos, node_color=node_colors, node_size=50, with_labels=False, edge_color='gray', cmap=plt.cm.jet)
    plt.show()

    # Step 5: Visualize the Graph using Batch Processing
    logging.info("Visualizing the graph in batches...")
    batch_process_graph(G, batch_size=20)  # Adjust batch_size based on your needs

if __name__ == "__main__":
    main()
