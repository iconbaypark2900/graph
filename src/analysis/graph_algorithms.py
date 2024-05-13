# graph_algorithms.py
import networkx as nx
from networkx.algorithms import community

def calculate_centrality(G):
    """
    Calculates and returns the degree centrality of nodes in the graph.
    """
    return nx.degree_centrality(G)

def detect_communities(G):
    """
    Uses the Louvain method to detect communities in the graph.
    """
    communities_generator = community.louvain_communities(G, seed=42)
    return communities_generator

if __name__ == "__main__":
    # Example usage with a hypothetical graph instance
    G = nx.DiGraph()
    # Populate G with example data for demonstration
    G.add_node(1, type='User')
    G.add_node(2, type='User')
    G.add_node(3, type='User')
    G.add_node(4, type='Product')
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    
    centrality = calculate_centrality(G)
    print("Centrality:", centrality)
    communities = detect_communities(G)
    print("Communities detected:", list(communities))
